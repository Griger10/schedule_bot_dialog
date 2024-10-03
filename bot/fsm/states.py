from aiogram.fsm.state import State, StatesGroup


class MainFSM(StatesGroup):
    hello = State()