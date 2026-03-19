from aiogram import Router, F
from aiogram.types import Message

from keyboards.complaints_menu import complaints_menu
from keyboards.main_menu import main_menu
from utils.navigation import set_menu

router = Router()

@router.message(F.text == "📩 Мої Звернення")
async def complaints_menu_open(message: Message):
    await message.answer(
        "Розділ звернень громадян",
        reply_markup=complaints_menu
    )


@router.message(F.text == "⬅ Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Головне меню",
        reply_markup=main_menu
    )