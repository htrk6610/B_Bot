from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.main_menu import main_menu

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Вітаємо у боті Бучанської громади.\nОберіть потрібний розділ:",
        reply_markup=main_menu
    )