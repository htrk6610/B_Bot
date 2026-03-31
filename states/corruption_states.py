from aiogram.fsm.state import StatesGroup, State


class CorruptionState(StatesGroup):
    text = State()
    address = State()
    confirm = State()