from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.main_menu import main_menu
from utils.navigation import set_menu

router = Router()


@router.message(F.text == "⛽ Пальне")
async def fuel(message: Message, state: FSMContext):
    await set_menu(state, "fuel")
    await message.answer("Інформація про пальне скоро буде доступна")


@router.message(F.text == "🪖 Ветеранам та їх родинам")
async def veterans(message: Message, state: FSMContext):
    await set_menu(state, "veterans")
    await message.answer("Розділ для ветеранів у розробці")


@router.message(F.text == "🤝 Соціальні послуги")
async def social(message: Message, state: FSMContext):
    await set_menu(state, "social")
    await message.answer("Соціальні послуги у розробці")


@router.message(F.text == "🏠 Пункти Незламності")
async def points(message: Message, state: FSMContext):
    await set_menu(state, "points")
    await message.answer("Пункти незламності у розробці")


@router.message(F.text == "🚨 Повідомлення про корупцію")
async def corruption(message: Message, state: FSMContext):
    await set_menu(state, "corruption")
    await message.answer("Повідомлення про корупцію")


@router.message(F.text == "📩 Мої звернення")
async def complaints(message: Message, state: FSMContext):
    await set_menu(state, "complaints")
    await message.answer("Ваші звернення")