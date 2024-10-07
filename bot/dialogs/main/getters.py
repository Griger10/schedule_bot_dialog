from aiogram.types import User
from aiogram_dialog import DialogManager
from bot.db.repositories.group_realization import GroupRealization
from bot.db.repositories.schedule_realization import ScheduleRealization
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession


async def get_hello(dialog_manager: DialogManager, i18n: TranslatorRunner,
                    event_from_user: User, **kwargs):
    username = event_from_user.first_name
    return {'hello_user': i18n.start.start(username=username)}


async def get_groups(session: AsyncSession, dialog_manager: DialogManager, **kwargs):
    group_repository = GroupRealization(session=session)
    groups = await group_repository.get_groups()
    return {'groups': groups}


async def get_welcome(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs):
    return {'welcome_user': i18n.welcome.user()}


async def get_days(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    schedule_realization = ScheduleRealization(session)
    type_of_week = await schedule_realization.get_week_type()
    types_of_week = {0: 'Числитель', 1: 'Знаменатель'}
    days = [
        ('Понедельник', 1),
        ('Вторник', 2),
        ('Среда', 3),
        ('Четверг', 4),
        ('Пятница', 5)
        ]
    return {'days': days, 'type_of_week': f'Текущая неделя - <b>{types_of_week[type_of_week]}</b>\n'}


async def get_day_schedule(dialog_manager: DialogManager, **kwargs):
    schedule = dialog_manager.dialog_data.get('day_schedule')
    return {'day_schedule': schedule}
