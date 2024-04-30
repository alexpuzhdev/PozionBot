from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
import os
from app.Database.DataBaseManager import DatabaseManager

import random
import string


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
db_manager = DatabaseManager('Database.sqlite')


class GenerateReferralLink:
    @staticmethod
    def get_ref():
        # Генерируем 10 случайных цифр
        random_digits = ''.join(random.choices(string.digits, k=10))
        # Составляем реферальную ссылку
        referral_link = f'https://t.me/NepalStore?start=#ref{random_digits}'
        return referral_link


class UserData:
    @staticmethod
    async def user_data_message(message):
        user_id = message.from_user.id
        first_name_tg = message.from_user.first_name
        last_name_tg = message.from_user.last_name
        username_tg = message.from_user.username
        user_position = 'Пользователь'
        count_orders = '0'
        city = 'Не указан'
        address = 'Не указан'
        firstname = 'Не указан'
        surname = 'Не указано'
        lastname = 'Не указано'
        phone_number = 'Не указан'
        active_delivery = False
        pers_loyalty = '0 %'
        pers_referal_link = GenerateReferralLink.get_ref()
        from_referal_link = None
#16
        return {
            'user_id': user_id,
            'first_name_tg': first_name_tg,
            'last_name_tg': last_name_tg,
            'username_tg': username_tg,
            'user_position': user_position,
            'count_orders': count_orders,
            'city': city,
            'address': address,
            'firstname': firstname,
            'surname': surname,
            'lastname': lastname,
            'phone_number': phone_number,
            'active_delivery': active_delivery,
            'pers_loyalty': pers_loyalty,
            'pers_referal_link': pers_referal_link,
            'from_referal_link': from_referal_link,
        }
#16




