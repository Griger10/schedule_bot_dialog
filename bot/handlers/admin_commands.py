from aiogram import Router, F
from aiogram.filters import Command, MagicData
from aiogram.types import Message
from bot.db.repositories.group_realization import GroupRealization
from bot.db.repositories.lesson_realization import LessonRealization
from bot.infrastructure.scheduler.tasks import change_type_of_week
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession


router = Router()

router.message.filter(MagicData(F.event.chat.id.in_(F.admin_ids)))


@router.message(Command(commands=['admin']))
async def admin(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.admin.info())


@router.message(Command(commands=['add_group']))
async def add_group(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    group_name = message.text.split()[1].strip()
    group_repository = GroupRealization(session)
    await group_repository.add_group(group_name)
    await message.answer(i18n.group.success(group_name=group_name))


@router.message(Command(commands=['add_lesson']))
async def add_group(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    lesson_name = message.text.split()[1].strip()
    group_repository = LessonRealization(session)
    await group_repository.add_lesson(lesson_name)
    await message.answer(i18n.lesson.success(lesson_name=lesson_name))


@router.message(Command(commands=['add_lesson_to_schedule']))
async def add_lesson_to_schedule(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    pass


@router.message(Command(commands=['change_week_type']))
async def change_week_type(message: Message, i18n: TranslatorRunner, session: AsyncSession):
    await change_type_of_week.kiq(session)
    await message.answer(i18n.type_of_week.change_success())
