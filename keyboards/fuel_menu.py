from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fuel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⛽ Ціни в області")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)