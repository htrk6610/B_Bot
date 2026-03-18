from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

weather_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌤 Погода зараз")],
        [KeyboardButton(text="📅 Прогноз на завтра")],
        [KeyboardButton(text="🔔 Підписка на погоду")],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)