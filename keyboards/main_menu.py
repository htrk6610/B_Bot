from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌤 Погода"),
            KeyboardButton(text="🌫 Якість повітря")
        ],
        [
            KeyboardButton(text="🚨 Повітряна тривога"),
            KeyboardButton(text="⚡ Відключення світла")
        ],
        [
            KeyboardButton(text="🏛 Моя Громада"),
            KeyboardButton(text="📩 Мої Звернення")
        ],
        [
            KeyboardButton(text="⭐ Мої підписки")
        ]
    ],
    resize_keyboard=True
)