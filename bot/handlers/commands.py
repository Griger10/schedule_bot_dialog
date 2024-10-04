from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()


@router.message(Command(commands=['start']))
async def start(message: Message, i18n: TranslatorRunner):
    await message.answer('test')
