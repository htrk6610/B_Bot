from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.weather_menu import weather_menu
from keyboards.main_menu import main_menu
from states.menu_states import MenuState
from utils.navigation import set_menu

router = Router()


@router.message(F.text == "🌤 Погода")
async def weather_menu_open(message: Message, state: FSMContext):
    await state.set_state(MenuState.weather)
    await set_menu(state, "weather")

    await message.answer(
        "Розділ погоди",
        reply_markup=weather_menu
    )

async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == MenuState.weather.state:
        await state.set_state(MenuState.main)
        await message.answer("Головне меню", reply_markup=main_menu)