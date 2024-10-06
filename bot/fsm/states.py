from aiogram.fsm.state import State, StatesGroup


class StartFSM(StatesGroup):
    hello = State()
    choose_group = State()
    welcome_message = State()


class MainFSM(StatesGroup):
    monday = State()
    tuesday = State()
    wednesday = State()
    thursday = State()
    friday = State()
