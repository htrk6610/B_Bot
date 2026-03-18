from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

alarm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚨 Статус тривоги")],
        [KeyboardButton(text="🔔 Підписка на тривогу")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)