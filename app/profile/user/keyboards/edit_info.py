from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           InlineKeyboardButton, KeyboardButton)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.types import WebAppInfo

edit_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ФИО', callback_data='edit_fio'),
     InlineKeyboardButton(text='Город', callback_data='edit_city')],
    [InlineKeyboardButton(text='Адрес', callback_data='edit_address'),
     InlineKeyboardButton(text='Номер телефона', callback_data='edit_phone_number')],
    [InlineKeyboardButton(text='🔙 Назад', callback_data='Профиль')],
    [InlineKeyboardButton(text='В главное меню', callback_data='main_menu')]
])

fsm_fio = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Редактировать имя', callback_data='edit_firstname'),
     InlineKeyboardButton(text='Редактировать фамилию', callback_data='edit_lastname')],
    [InlineKeyboardButton(text='Редактировать отчество', callback_data='edit_thridname')],
    [InlineKeyboardButton(text='Готово', callback_data='complete_fio')],
    [InlineKeyboardButton(text='❌ Отмена', callback_data='edit_info')]
])
