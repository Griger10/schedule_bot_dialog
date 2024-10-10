from aiogram.types import User, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select
from db.repositories.group_realization import GroupRealization
from db.repositories.schedule_realization import ScheduleRealization
from fsm.states import StartFSM, MainFSM


async def set_group_dialog(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(StartFSM.choose_group)
    await callback.answer()


async def choose_group(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    session = dialog_manager.middleware_data['session']
    group_repository = GroupRealization(session)
    await group_repository.set_group(int(item_id), callback.message.chat.id)
    await dialog_manager.switch_to(StartFSM.welcome_message)


async def day_schedule(callback: CallbackQuery, widget: Select,
                       dialog_manager: DialogManager, item_id: str):
    session = dialog_manager.middleware_data['session']
    schedule_repository = ScheduleRealization(session)
    lessons = await schedule_repository.get_schedule(callback.message.chat.id, int(item_id))
    res = '\n\n'.join(f"{ls[0]} пара в {ls[1]} --- <b>{ls[2]}</b>" for ls in lessons)
    dialog_manager.dialog_data.update(day_schedule=res)
    await dialog_manager.switch_to(MainFSM.day_schedule)


async def start_schedule(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainFSM.choose_day)
