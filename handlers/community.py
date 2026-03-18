from aiogram import Router, F
from aiogram.types import Message

from keyboards.community_menu import community_menu
from keyboards.main_menu import main_menu

router = Router()

@router.message(F.text == "🏛 Моя Громада")
async def community_menu_open(message: Message):
    await message.answer(
        "Інформація про громади району",
        reply_markup=community_menu
    )


@router.message(F.text == "⬅ Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Головне меню",
        reply_markup=main_menu
    )