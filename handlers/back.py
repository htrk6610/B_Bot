from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.navigation import back

from keyboards.main_menu import main_menu
from keyboards.weather_menu import weather_menu
from keyboards.air_menu import air_menu
from keyboards.alarm_menu import alarm_menu
from keyboards.power_menu import power_menu
from keyboards.community_menu import community_menu
from keyboards.complaints_menu import complaints_menu

router = Router()


@router.message(F.text == "⬅ Назад")
async def back_handler(message: Message, state: FSMContext):
    previous_menu = await back(state)

    if previous_menu == "main":
        await message.answer("Головне меню", reply_markup=main_menu)

    elif previous_menu == "weather":
        await message.answer("Погода", reply_markup=weather_menu)

    elif previous_menu == "air":
        await message.answer("Якість повітря", reply_markup=air_menu)

    elif previous_menu == "alarm":
        await message.answer("Тривога", reply_markup=alarm_menu)

    elif previous_menu == "power":
        await message.answer("Світло", reply_markup=power_menu)

    elif previous_menu == "community":
        await message.answer("Громада", reply_markup=community_menu)

    elif previous_menu == "complaints":
        await message.answer("Звернення", reply_markup=complaints_menu)