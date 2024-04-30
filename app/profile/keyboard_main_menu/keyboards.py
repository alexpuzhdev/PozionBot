from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

main_kb = [
    [KeyboardButton(text='Профиль'),
     KeyboardButton(text='FAQ')],
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True)

profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мои покупки', callback_data='my_purchase'),
     InlineKeyboardButton(text='Статус доставки', callback_data='delivery_status')],
    [InlineKeyboardButton(text='Корзина', callback_data='my_cart'),
     InlineKeyboardButton(text='Избранное', callback_data='my_favorites')],
    [InlineKeyboardButton(text='Редактировать данные', callback_data='edit_info')],
    [InlineKeyboardButton(text='🔙 Главное меню', callback_data='main_menu')]
])