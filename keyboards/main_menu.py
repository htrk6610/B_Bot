from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⚡ Світло"),
            KeyboardButton(text="⛽ Пальне")
        ],
        [
            KeyboardButton(text="🌤 Погода"),
            KeyboardButton(text="🌫 Якість повітря")
        ],
        [
            KeyboardButton(text="🪖 Ветеранам та їх родинам"),
            KeyboardButton(text="🤝 Соціальні послуги")
        ],
        [
            KeyboardButton(text="🏠 Пункти Незламності"),
            KeyboardButton(text="🚨 Повітряна тривога")
        ],
        [
            KeyboardButton(text="🚨 Повідомлення про корупцію"),
            KeyboardButton(text="📩 Мої звернення")
        ]
    ],
    resize_keyboard=True
)