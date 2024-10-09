import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram_dialog import setup_dialogs
from bot.infrastructure.scheduler.taskiq_broker import redis_source, broker
from bot.infrastructure.scheduler.tasks import change_type_of_week_automation
from bot.dialogs.main.dialogs import start_dialog, schedule_dialog
from bot.handlers import commands, admin_commands, other_handlers
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DatabaseMiddleware
from bot.middlewares.type_of_week import TypeOfWeekMiddleware
from bot.middlewares.users import TrackAllUsersMiddleware
from bot.utils.i18n import create_translator_hub
from bot.config.config import load_config, load_database
from aiogram import Bot, Dispatcher
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


async def main():
    config = load_config()
    database_config = load_database()

    engine = create_async_engine(url=database_config.dsn, echo=database_config.is_echo)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    redis = Redis(host='redis', port=6379)
    storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))

    async with engine.begin() as connection:
        await connection.execute(text('SELECT 1'))

    translator_hub = create_translator_hub()
    dp = Dispatcher(storage=storage, admin_ids=config.admin_ids)
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.update.outer_middleware(DatabaseMiddleware(session_maker))
    dp.update.outer_middleware(TypeOfWeekMiddleware())
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    dp.include_router(admin_commands.router)
    dp.include_router(commands.router)
    dp.include_router(start_dialog)
    dp.include_router(schedule_dialog)

    setup_dialogs(dp)

    dp.include_router(other_handlers.router)

    await broker.startup()

    await change_type_of_week_automation.schedule_by_cron(
        source=redis_source,
        cron='0 20 * * 5')

    print('start bot...')
    await dp.start_polling(bot, _translator_hub=translator_hub, redis_source=redis_source)
    await broker.shutdown()


if __name__ == '__main__':
    if sys.platform == 'win32':
        from asyncio import WindowsSelectorEventLoopPolicy
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
