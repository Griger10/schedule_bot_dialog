from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select
from aiogram_dialog.widgets.text import Format, Const
from bot.dialogs.main.getters import get_hello, get_groups
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
    ),
    Window(
        Const(text='Выберите группу из списка:'),
        Select(
            Format('{item[2]}'),
            id='group',
            item_id_getter=lambda x: x[0],
            items='groups',
            on_click=group_setting
        ),
        state=StartFSM.choose_group,
        getter=get_groups
    )
)
