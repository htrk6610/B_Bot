# handlers/light.py
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.light_menu import light_menu
from utils.navigation import set_menu

router = Router()


@router.message(F.text == "⚡ Світло")
async def light_menu_open(message: Message, state: FSMContext):
    await set_menu(state, "light")

    await message.answer(
        "Інформація щодо електропостачання",
        reply_markup=light_menu
    )

@router.message(F.text == "🤖 Чат-бот ДТЕК")
async def dtek(message: Message):
    await message.answer(
        "Скористайтесь офіційним ботом ДТЕК:\n\n"
        "Telegram:\nhttps://t.me/DTEKKyivRegionElektromerezhiBot\n\n"
        "Viber:\nhttp://www.viber.com/dtekkyivregionelektromerezhi"
    )

@router.message(F.text == "📞 Контакти")
async def contacts(message: Message):
    await message.answer(
        "Повідомити про проблему:\n\n"
        "📞 +380674957040\n"
        "📞 +380994957040\n"
        "📞 +380934957040"
    )

@router.message(F.text == "📅 Графік відключень")
async def contacts2(message: Message):
    await message.answer(
        "Розділ у розробці. Слідкуйте за оновленнями!"
    )