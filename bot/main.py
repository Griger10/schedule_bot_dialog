import sys
from asyncio import WindowsSelectorEventLoopPolicy
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import load_config
from aiogram import Bot, Dispatcher
import asyncio


async def main():
    config = await load_config()
    dp = Dispatcher()
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
