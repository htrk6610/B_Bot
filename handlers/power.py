from aiogram import Router, F
from aiogram.types import Message

from keyboards.power_menu import power_menu
from keyboards.main_menu import main_menu
from utils.navigation import set_menu

router = Router()

@router.message(F.text == "⚡ Відключення світла")
async def power_menu_open(message: Message):
    await message.answer(
        "Інформація про відключення світла",
        reply_markup=power_menu
    )


@router.message(F.text == "⬅ Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Головне меню",
        reply_markup=main_menu
    )