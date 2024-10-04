from aiogram.types import User
from aiogram_dialog import DialogManager
from bot.fsm.states import StartFSM


async def set_group(dialog_manager: DialogManager, event_from_user: User):
    await dialog_manager.switch_to(StartFSM.choose_group)
