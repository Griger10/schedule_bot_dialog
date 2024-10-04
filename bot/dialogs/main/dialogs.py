from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format, Const
from bot.dialogs.main.getters import get_hello
from bot.dialogs.main.handlers import set_group
from bot.fsm.states import StartFSM

start_dialog = Dialog(
    Window(
        Format('{hello_user}'),
        Button(Const('Выбрать группу'),
               id='set_group',
               on_click=set_group),
        getter=get_hello,
        state=StartFSM.hello
    )
)
