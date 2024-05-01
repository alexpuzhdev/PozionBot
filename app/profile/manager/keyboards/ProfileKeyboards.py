from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

profile_manager = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Список тикетов', callback_data='ticket_list'),
         InlineKeyboardButton(text='Открытые тикеты', callback_data='open_tickets_list')],
        [InlineKeyboardButton(text='Создать заказ', callback_data='create_order'),
         InlineKeyboardButton(text='Таблица байеров', callback_data='table_buyers')],
        [InlineKeyboardButton(text='🔙 Главное меню', callback_data='main_menu')]
])
