# keyboards/veterans_menu.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

veterans_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Ветеран PRO"),
            KeyboardButton(text="👨‍💼 Фахівці супроводу"),
        ],

        [
            KeyboardButton(text="📍 Де знайти фахівця"),
            KeyboardButton(text="📄 Надання статусів"),
        ],

        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)