from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession


async def get_hello(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        event_from_user: User,
        **kwargs
):
    first_name = event_from_user.first_name
    return {'hello_user_text': i18n.start.text(first_name=first_name)}


async def get_groups(
        session: AsyncSession, dialog_manager: DialogManager, **kwargs
):
    pass


async def get_welcome(
        dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
):
    return {'welcome_user_text': i18n.welcome.user()}


async def get_days(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    pass


async def get_day_schedule(dialog_manager: DialogManager, **kwargs):
    pass
