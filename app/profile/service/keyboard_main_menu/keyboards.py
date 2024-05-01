from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = [
    [KeyboardButton(text='Профиль'),
     KeyboardButton(text='FAQ')],
]

main = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)
