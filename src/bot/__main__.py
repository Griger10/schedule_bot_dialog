import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram_dialog import setup_dialogs
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.dialogs import start_dialog, schedule_dialog
from bot.handlers import commands, admin_commands, other_handlers
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DatabaseMiddleware
from bot.middlewares.users import TrackAllUsersMiddleware
from bot.utils.i18n import create_translator_hub
from core.config import Config


async def main():
    config = Config()

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
    bot = Bot(
        token=config.bot_config.token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
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

    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    asyncio.run(main())
