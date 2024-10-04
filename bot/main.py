import sys
from asyncio import WindowsSelectorEventLoopPolicy
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from bot.utils.i18n import create_translator_hub
from config import load_config, load_database
from aiogram import Bot, Dispatcher
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine


async def main():
    storage = MemoryStorage()
    config = await load_config()
    database_config = await load_database()
    engine = create_async_engine(url=database_config.dsn, echo=database_config.is_echo)
    translator_hub = create_translator_hub()
    dp = Dispatcher(storage=storage)
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    print('start bot...')
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
