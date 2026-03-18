from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

air_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌫 Якість повітря зараз")],
        [KeyboardButton(text="🔔 Підписка на повітря")],
        [KeyboardButton(text="📉 Різкі зміни якості")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)