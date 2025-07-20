from aiogram import Bot
from aiogram.types import BotCommand
from fluentogram import TranslatorRunner


async def set_main_menu(bot: Bot, i18n: TranslatorRunner):
    bot_commands = [
        BotCommand(command='/schedule', description=i18n.schedule.short_info()),
        BotCommand(command='/start', description=i18n.start.short_info()),
        BotCommand(command='/help', description=i18n.help.short_info()),
        BotCommand(command='/contacts', description=i18n.contacts.short_info())
    ]
    await bot.set_my_commands(bot_commands)
