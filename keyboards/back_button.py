from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)