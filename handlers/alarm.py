from aiogram import Router, F
from aiogram.types import Message

from keyboards.alarm_menu import alarm_menu
from keyboards.main_menu import main_menu

router = Router()

@router.message(F.text == "🚨 Повітряна тривога")
async def alarm_menu_open(message: Message):
    await message.answer(
        "Інформація про повітряні тривоги",
        reply_markup=alarm_menu
    )


@router.message(F.text == "⬅ Назад")
async def back_to_main(message: Message):
    await message.answer(
        "Головне меню",
        reply_markup=main_menu
    )