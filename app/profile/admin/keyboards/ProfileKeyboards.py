from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

profile_admin = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Список пользователей', callback_data='users_list'),
         InlineKeyboardButton(text='Список персонала', callback_data='reps_list')],
        [InlineKeyboardButton(text='Таблица менеджеров', callback_data='table_managers'),
         InlineKeyboardButton(text='Таблица байеров', callback_data='table_buyers')],
        [InlineKeyboardButton(text='🔙 Главное меню', callback_data='main_menu')]
])
