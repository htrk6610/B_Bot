from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.fuel_menu import fuel_menu
from utils.navigation import set_menu
from services.fuel_service import get_fuel_prices

router = Router()


@router.message(F.text == "⛽ Пальне")
async def fuel_menu_open(message: Message, state: FSMContext):
    await set_menu(state, "fuel")

    await message.answer(
        "Інформація про пальне",
        reply_markup=fuel_menu
    )


@router.message(F.text == "⛽ Ціни в області")
async def fuel_prices(message: Message):
    data = await get_fuel_prices()

    if not data:
        await message.answer("❌ Не вдалося отримати дані")
        return

    text = "⛽ Ціни на пальне (Київська область):\n\n"

    for item in data:
        text += f"• {item}\n"

    await message.answer(text)