# keyboards/light_menu.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

light_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 Чат-бот ДТЕК")],
        [KeyboardButton(text="📞 Контакти")],
        [KeyboardButton(text="📅 Графік відключень")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)