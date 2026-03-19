from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.main_menu import main_menu
from states.menu_states import MenuState
from utils.navigation import set_menu

router = Router()


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await state.set_state(MenuState.main)
    await set_menu(state, "main")

    await message.answer(
        "Вітаємо у боті Бучанської Громади.\nОберіть розділ:",
        reply_markup=main_menu
    )