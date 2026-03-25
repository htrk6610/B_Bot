from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.phone_request import phone_keyboard
from utils.allowed_users import ALLOWED_PHONES
from keyboards.main_menu import main_menu
from states.menu_states import MenuState
from utils.navigation import set_menu
from database.db import cursor, conn

router = Router()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    telegram_id = message.from_user.id

    cursor.execute(
        "SELECT is_allowed FROM users WHERE telegram_id = ?",
        (telegram_id,)
    )
    user = cursor.fetchone()

    if user:
        if user[0] == 1:
            await set_menu(state, "main")

            await message.answer(
                "З поверненням 👋",
                reply_markup=main_menu
            )
        else:
            await message.answer("⛔ Доступ заборонено")
    else:
        await message.answer(
            "Для доступу поділіться номером телефону:",
            reply_markup=phone_keyboard
        )

@router.message(F.contact)
async def get_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    telegram_id = message.from_user.id

    is_allowed = 1 if phone in ALLOWED_PHONES else 0

    # сохраняем в БД
    cursor.execute(
        "INSERT INTO users (telegram_id, phone, is_allowed) VALUES (?, ?, ?)",
        (telegram_id, phone, is_allowed)
    )
    conn.commit()

    if is_allowed:
        await set_menu(state, "main")

        await message.answer(
            "Доступ дозволено ✅",
            reply_markup=main_menu
        )
    else:
        await message.answer("⛔ Доступ заборонено")

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await state.set_state(MenuState.main)
    await set_menu(state, "main")

    await message.answer(
        "Вітаємо у боті Бучанської Громади.\nОберіть розділ:",
        reply_markup=main_menu
    )