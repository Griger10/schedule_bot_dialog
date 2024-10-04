from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


async def get_hello(dialog_manager: DialogManager, i18n: TranslatorRunner,
                    event_from_user: User, **kwargs):
    username = event_from_user.first_name
    return {'hello_user': i18n.start.start(username=username)}
