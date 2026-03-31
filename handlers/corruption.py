from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.corruption_states import CorruptionState
from utils.navigation import set_menu
from utils.admins import ADMINS

router = Router()


@router.message(F.text == "🚨 Повідомлення про корупцію")
async def start_report(message: Message, state: FSMContext):
    await set_menu(state, "corruption")

    await state.set_state(CorruptionState.text)

    await message.answer("Опишіть ситуацію:")

@router.message(CorruptionState.text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)

    await state.set_state(CorruptionState.address)
    await message.answer("Вкажіть адресу або місце:")

@router.message(CorruptionState.address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    data = await state.get_data()

    await state.set_state(CorruptionState.confirm)

    await message.answer(
        f"Перевірте дані:\n\n"
        f"{data['text']}\n"
        f"{data['address']}\n\n"
        "Напишіть 'так' для відправки"
    )

@router.message(CorruptionState.confirm)
async def confirm(message: Message, state: FSMContext, bot: Bot):
    if message.text.lower() == "так":
        data = await state.get_data()

        text = (
            "🚨 НОВЕ ПОВІДОМЛЕННЯ ПРО КОРУПЦІЮ\n\n"
            f"{data['text']}\n\n"
            f"📍 {data['address']}"
        )

        for admin_id in ADMINS:
            await bot.send_message(admin_id, text)

        await message.answer("✅ Повідомлення надіслано")
    else:
        await message.answer("❌ Скасовано")

    await state.clear()