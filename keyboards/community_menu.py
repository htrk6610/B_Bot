from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

community_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏛 Бучанська РДА")],
        [KeyboardButton(text="🏘 ОТГ району")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)