from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select, Group
from aiogram_dialog.widgets.text import Format, Const
from bot.dialogs.main.getters import get_hello, get_groups, get_welcome
from bot.dialogs.main.handlers import set_group_dialog, choose_group
from bot.fsm.states import StartFSM, MainFSM
from bot.utils.dialogs import go_next

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
        Group(
            Select(
                Format('{item.name}'),
                id='group',
                item_id_getter=lambda x: x.id,
                items='groups',
                on_click=choose_group
            ),
            width=1
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


schedule_dialog = Dialog(
    Window(
        Format("{monday_schedule}"),
        Button(Const('>>'), id='mon_button', on_click=go_next),
        state=MainFSM.monday,
        getter=monday_schedule
    )
)
