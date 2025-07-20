from aiogram import Router, F
from aiogram.filters import Command, MagicData
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()

router.message.filter(MagicData(F.event.chat.id.in_(F.admin_ids)))


@router.message(Command(commands=['admin']))
async def admin(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.admin.info())


@router.message(Command(commands=['add_group']))
async def add_group(message: Message, i18n: TranslatorRunner):
    pass


@router.message(Command(commands=['add_lesson']))
async def add_group(message: Message, i18n: TranslatorRunner):
    lesson_name = message.text.split()[1].strip()
    await message.answer(i18n.lesson.success(lesson_name=lesson_name))


@router.message(Command(commands=['add_lesson_to_schedule']))
async def add_lesson_to_schedule(message: Message, i18n: TranslatorRunner):
    pass


@router.message(Command(commands=['change_week_type']))
async def change_week_type(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.type_of_week.change_success())




