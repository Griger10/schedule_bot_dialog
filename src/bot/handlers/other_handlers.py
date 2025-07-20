from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()


@router.message()
async def other_messages(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.no.answer())
