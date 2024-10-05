from aiogram.types import User, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from bot.db.repositories.group_realization import GroupRealization
from bot.fsm.states import StartFSM
from sqlalchemy.ext.asyncio import AsyncSession


async def set_group_dialog(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(StartFSM.choose_group)
    await callback.answer()


async def choose_group(callback: CallbackQuery, button: Button, item_id: str,
                       dialog_manager: DialogManager, session: AsyncSession):
    group_repository = GroupRealization(session)
    await group_repository.set_group(int(item_id), callback.message.chat.id)
    await dialog_manager.switch_to(StartFSM.welcome_message)
    await callback.answer()

