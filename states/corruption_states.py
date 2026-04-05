from aiogram.fsm.state import StatesGroup, State


class CorruptionState(StatesGroup):
    start = State()
    problem = State()
    text = State()
    address = State()
    confirm = State()