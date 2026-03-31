from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.main_menu import main_menu
from utils.navigation import set_menu

router = Router()

@router.message(F.text == "🤝 Соціальні послуги")
async def social(message: Message, state: FSMContext):
    await set_menu(state, "social")
    await message.answer("Розділ у розробці")


@router.message(F.text == "🏠 Пункти Незламності")
async def points(message: Message, state: FSMContext):
    await set_menu(state, "points")
    await message.answer("Розділ у розробці")


@router.message(F.text == "📩 Мої звернення")
async def complaints(message: Message, state: FSMContext):
    await set_menu(state, "complaints")
    await message.answer("Розділ у розробці")

@router.message(F.text == "🌫 Якість повітря")
async def air(message: Message, state: FSMContext):
    await set_menu(state, "air")
    await message.answer("Розділ у розробці")

@router.message(F.text == "🚨 Повітряна тривога")
async def alarm(message: Message, state: FSMContext):
    await set_menu(state, "alarm")
    await message.answer("Розділ у розробці")