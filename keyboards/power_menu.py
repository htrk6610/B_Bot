from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

power_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⚡ Вибір групи")],
        [KeyboardButton(text="📅 Графік сьогодні")],
        [KeyboardButton(text="📅 Графік завтра")],
        [KeyboardButton(text="🔔 Підписка на графік")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)