from aiogram.fsm.state import State, StatesGroup


class StartFSM(StatesGroup):
    hello = State()
    choose_group = State()
    welcome_message = State()


class MainFSM(StatesGroup):
    choose_day = State()
    day_schedule = State()
