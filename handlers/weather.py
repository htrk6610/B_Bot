from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.weather_states import WeatherState
from services.weather_service import get_weather

from keyboards.weather_menu import weather_menu
from keyboards.main_menu import main_menu
from states.menu_states import MenuState
from utils.navigation import set_menu

router = Router()

@router.message(F.text == "🌤 Погода")
async def weather_menu_open(message: Message, state: FSMContext):
    await set_menu(state, "weather")

    await message.answer(
        "Розділ погоди",
        reply_markup=weather_menu
    )

@router.message(F.text == "🌤 Погода зараз")
async def ask_city(message: Message, state: FSMContext):
    await state.set_state(WeatherState.waiting_for_city)

    await message.answer("Введіть назву населеного пункту:")

@router.message(WeatherState.waiting_for_city)
async def get_city_weather(message: Message, state: FSMContext):
    city = message.text

    weather = await get_weather(city)

    if not weather:
        await message.answer("❌ Не вдалося знайти населений пункт")
        return

    text = (
        f"📍 {weather['city']}\n"
        f"🌡 Температура: {weather['temp']}°C\n"
        f"☁️ {weather['description']}"
    )

    await message.answer(text)

    await state.clear()

async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == MenuState.weather.state:
        await state.set_state(MenuState.main)
        await message.answer("Головне меню", reply_markup=main_menu)