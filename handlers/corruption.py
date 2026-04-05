from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.db import cursor
from states.corruption_states import CorruptionState
from utils.navigation import set_menu
from utils.admins import ADMINS

router = Router()

@router.message(F.text == "🚨 Повідомлення про корупцію")
async def start_report(message: Message, state: FSMContext):
    await set_menu(state, "corruption")
    await state.set_state(CorruptionState.problem)

    await message.answer("📌 Вкажіть суть проблеми:")

@router.message(CorruptionState.problem)
async def get_problem(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)

    await state.set_state(CorruptionState.text)
    await message.answer("📝 Опишіть деталі ситуації:")

@router.message(CorruptionState.text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)

    await state.set_state(CorruptionState.address)
    await message.answer("📍 Вкажіть місце:")

@router.message(CorruptionState.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    data = await state.get_data()

    await state.set_state(CorruptionState.confirm)

    await message.answer(
        f"Перевірте дані:\n\n"
        f"📌 Суть: {data['problem']}\n"
        f"📝 Опис: {data['text']}\n"
        f"📍 Адреса: {data['address']}\n\n"
        "Напишіть 'так' для відправки"
    )

@router.message(CorruptionState.confirm)
async def confirm(message: Message, state: FSMContext, bot: Bot):
    if message.text.lower() == "так":
        data = await state.get_data()

        user_id = message.from_user.id

        cursor.execute(
            "SELECT phone FROM users WHERE telegram_id = ?",
            (user_id,)
        )
        user = cursor.fetchone()

        phone = user[0] if user else "невідомо"

        text = (
            "🚨 НОВЕ ПОВІДОМЛЕННЯ ПРО КОРУПЦІЮ\n\n"
            f"📌 Суть:\n{data['problem']}\n\n"
            f"📝 Опис:\n{data['text']}\n\n"
            f"📍 Адреса:\n{data['address']}\n\n"
            f"👤 Користувач:\n"
            f"ID: {user_id}\n"
            f"Телефон: {phone}"
        )

        for admin_id in ADMINS:
            await bot.send_message(admin_id, text)

        await message.answer("✅ Повідомлення надіслано")
    else:
        await message.answer("❌ Скасовано")

    await state.clear()