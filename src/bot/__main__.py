import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram_dialog import setup_dialogs
from dishka.integrations.aiogram import setup_dishka as setup_aiogram_dishka
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.dialogs import schedule_dialog, start_dialog
from bot.handlers import admin_commands, commands, other_handlers
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DatabaseMiddleware
from bot.middlewares.users import TrackAllUsersMiddleware
from bot.utils.i18n import create_translator_hub
from core.config import Config
from core.di.ioc import create_container
from core.logging import configure_logging

configure_logging()

logger = logging.getLogger(__name__)


async def main() -> None:
    config = Config()

    container = create_container()

    engine = create_async_engine(
        url=config.postgres_config.database_url,
    )
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    redis = Redis(
        host=config.redis_config.host,
        port=config.redis_config.port,
    )
    storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(
            with_destiny=True
        )
    )

    translator_hub = create_translator_hub()
    dp = Dispatcher(
        storage=storage,
        admin_ids=config.bot_config.admin_ids
    )
    bot = await container.get(Bot)

    setup_aiogram_dishka(
        router=dp,
        container=container,
        auto_inject=True,
    )

    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.update.outer_middleware(DatabaseMiddleware(session_maker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    dp.include_router(admin_commands.router)
    dp.include_router(commands.router)
    dp.include_router(start_dialog)
    dp.include_router(schedule_dialog)

    setup_dialogs(dp)

    dp.include_router(other_handlers.router)

    logger.info("Start bot...")
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())
