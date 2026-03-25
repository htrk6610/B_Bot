from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

weather_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌤 Погода зараз")],
        [KeyboardButton(text="📢 Розсилка (в розробці)")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)