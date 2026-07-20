from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Каталог"),
            KeyboardButton(text="👤 Профиль"),
        ],
        [
            KeyboardButton(text="💰 Баланс"),
        ],
    ],
    resize_keyboard=True,
)