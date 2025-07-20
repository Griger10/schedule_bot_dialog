from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hlink
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from bot.fsm.states import StartFSM, MainFSM
from bot.utils.main_menu import set_main_menu

router = Router()


@router.message(Command(commands=['start']))
async def start(message: Message, dialog_manager: DialogManager, bot: Bot, i18n: TranslatorRunner):
    await set_main_menu(bot, i18n)
    await dialog_manager.start(StartFSM.hello, mode=StartMode.RESET_STACK)


@router.message(Command(commands=['schedule']))
async def schedule(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainFSM.choose_day, mode=StartMode.RESET_STACK)


@router.message(Command(commands=['help']))
async def help_(message: Message, dialog_manager: DialogManager, i18n: TranslatorRunner):
    await message.answer(i18n.help.full())


@router.message(Command(commands=['contacts']))
async def contacts(message: Message, dialog_manager: DialogManager, i18n: TranslatorRunner):
    text = i18n.contacts.full() + ' ' + hlink(i18n.contacts.link(), 'https://t.me/griger10')
    await message.answer(text)
