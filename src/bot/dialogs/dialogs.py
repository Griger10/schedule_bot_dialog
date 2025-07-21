from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Url
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.getters import get_day_schedule, get_days, get_groups, get_hello, get_welcome
from bot.dialogs.handlers import choose_group, day_schedule, set_group_dialog, start_schedule
from bot.fsm.states import MainFSM, StartFSM
from bot.utils.dialogs import go_back

start_dialog = Dialog(
    Window(
        Format("{hello_user_text}"),
        Button(
            Const("Выбрать группу"),
            id="set_group",
            on_click=set_group_dialog
        ),
        getter=get_hello,
        state=StartFSM.hello
    ),
    Window(
        Const(text="Выберите группу из списка:"),
        Column(
            Select(
                Format("{item.name}"),
                id="group",
                item_id_getter=lambda x: x.id,
                items="groups",
                on_click=choose_group
            ),
        ),
        state=StartFSM.choose_group,
        getter=get_groups
    ),
    Window(
        Format("{welcome_user_text}"),
        Button(Const("Перейти к расписанию"), id="go_schedule", on_click=start_schedule),
        getter=get_welcome,
        state=StartFSM.welcome_message,
    )
)

schedule_dialog = Dialog(
    Window(
        Format("{type_of_week}"),
        Const("Выберите день недели:"),
        Group(
            Select(
                Format("{item[0]}"),
                id="day",
                item_id_getter=lambda x: x[1],
                items="days",
                on_click=day_schedule,
            ),
            width=1
        ),
        getter=get_days,
        state=MainFSM.choose_day
    ),
    Window(
        Const("Расписание на день:\n"),
        Format("{day_schedule}"),
        Column(
            Url(
                text=Const("Расписание на сайте ВлГУ"),
                url=Const(
                    "https://www.vlsu.ru/fileadmin/Dispetcher/2024-2025/osen/KITP.pdf"
                ),
                id="site_button"),
            Button(Const("Назад"),
                   id="back_button",
                   on_click=go_back)),
        state=MainFSM.day_schedule,
        getter=get_day_schedule
    )
)
