from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.phone_request import phone_keyboard
from utils.allowed_users import ALLOWED_PHONES
from keyboards.main_menu import main_menu
from states.menu_states import MenuState
from utils.navigation import set_menu

router = Router()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer(
        "Для доступу до бота поділіться номером телефону:",
        reply_markup=phone_keyboard
    )

@router.message(F.contact)
async def get_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number

    if phone in ALLOWED_PHONES:
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