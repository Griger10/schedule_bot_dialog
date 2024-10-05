from aiogram.types import User
from aiogram_dialog import DialogManager
from bot.db.repositories.group_realization import GroupRealization
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
