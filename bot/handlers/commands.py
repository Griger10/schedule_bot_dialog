from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from bot.fsm.states import StartFSM
from fluentogram import TranslatorRunner

router = Router()


@router.message(Command(commands=['start']))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(StartFSM.hello, mode=StartMode.RESET_STACK)
