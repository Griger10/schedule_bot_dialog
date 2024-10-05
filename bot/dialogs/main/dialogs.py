from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select
from aiogram_dialog.widgets.text import Format, Const
from bot.dialogs.main.getters import get_hello, get_groups, get_welcome
from bot.dialogs.main.handlers import set_group_dialog, choose_group
from bot.fsm.states import StartFSM

start_dialog = Dialog(
    Window(
        Format('{hello_user}'),
        Button(Const('Выбрать группу'),
               id='set_group',
               on_click=set_group_dialog),
        getter=get_hello,
        state=StartFSM.hello
    ),
    Window(
        Const(text='Выберите группу из списка:'),
        Select(
            Format('{item[2]}'),
            id='group',
            item_id_getter=lambda x: x[0],
            items='groups',
            on_click=choose_group
        ),
        state=StartFSM.choose_group,
        getter=get_groups
    ),
    Window(
        Format('{welcome_user}'),
        getter=get_welcome,
        state=StartFSM.welcome_message,
    )
)
