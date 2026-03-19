from aiogram.fsm.state import StatesGroup, State


class MenuState(StatesGroup):
    main = State()
    weather = State()
    air = State()
    alarm = State()
    power = State()
    community = State()
    complaints = State()