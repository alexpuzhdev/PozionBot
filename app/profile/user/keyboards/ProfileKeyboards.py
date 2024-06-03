from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

profile_user = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Активные заказы', callback_data='delivery_status'),
         InlineKeyboardButton(text='Завершенные', callback_data='my_cart')],
        # [InlineKeyboardButton(text='Избранное', callback_data='my_favorites')],
        [InlineKeyboardButton(text='Редактировать данные', callback_data='edit_info')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='main_menu')]
])
