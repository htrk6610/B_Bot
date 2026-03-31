from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tourism_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌳 Туристичні місця")],
        [KeyboardButton(text="🕯 Маршрут пам'яті")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)