import sys
from asyncio import WindowsSelectorEventLoopPolicy
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.middlewares.session import DatabaseMiddleware
from bot.utils.i18n import create_translator_hub
from config import load_config, load_database
from aiogram import Bot, Dispatcher
import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


async def main():
    storage = MemoryStorage()
    config = await load_config()
    database_config = await load_database()

    engine = create_async_engine(url=database_config.dsn, echo=database_config.is_echo)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as connection:
        await connection.execute(text('SELECT 1'))


    translator_hub = create_translator_hub()
    dp = Dispatcher(storage=storage)
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.update.outer_middleware(DatabaseMiddleware(session_maker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    print('start bot...')
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
