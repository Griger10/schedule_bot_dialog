from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from bot.dialogs.main.getters import get_hello
from bot.fsm.states import StartFSM

start_dialog = Dialog(
    Window(
        Format('{hello_user}'),
        getter=get_hello,
        state=StartFSM.hello
    )
)
