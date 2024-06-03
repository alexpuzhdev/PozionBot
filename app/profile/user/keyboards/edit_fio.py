from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

fsm_fio = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Редактировать имя', callback_data='edit_fio'),
     InlineKeyboardButton(text='Редактировать фамилию', callback_data='edit_city')],
    [InlineKeyboardButton(text='Редактировать отчество', callback_data='edit_address')],
    [InlineKeyboardButton(text='Готово', callback_data='complete_fio')],
    [InlineKeyboardButton(text='❌ Отмена', callback_data='edit_info')]
])