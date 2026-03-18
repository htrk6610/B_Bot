from aiogram import Router, F
from aiogram.types import Message

from keyboards.weather_menu import weather_menu
from keyboards.main_menu import main_menu

router = Router()


@router.message(F.text == "🌤 Погода")
async def weather_menu_open(message: Message):
    await message.answer(
        "Розділ погоди",
        reply_markup=weather_menu
    )


@router.message(F.text == "⬅ Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Головне меню",
        reply_markup=main_menu
    )