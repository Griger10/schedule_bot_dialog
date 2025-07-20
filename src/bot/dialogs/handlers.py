from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from bot.fsm.states import MainFSM, StartFSM


async def set_group_dialog(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.switch_to(StartFSM.choose_group)
    await callback.answer()


async def choose_group(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    pass


async def day_schedule(
        callback: CallbackQuery,
        widget: Select,
        dialog_manager: DialogManager,
        item_id: str
):
    pass


async def start_schedule(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainFSM.choose_day)
