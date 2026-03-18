from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

complaints_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📩 Подати звернення")],
        [KeyboardButton(text="📄 Мої звернення")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)