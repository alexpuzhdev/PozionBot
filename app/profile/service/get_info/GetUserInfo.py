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


class GetUserInfo:

    async def get_user_info_msg(self, message):
        user_id = message.from_user.id
        user_info = db_manager.get_actual_info_for_user(user_id)
        return user_info

    async def get_user_info_clb(self, callback):
        user_id = callback.from_user.id
        user_info = db_manager.get_actual_info_for_user(user_id)
        return user_info

    async def get_user_position_msg(self, message):
        user_id = message.from_user.id
        user_position = db_manager.get_user_position(user_id)
        return user_position

    async def get_user_position_clb(self, callback):
        user_id = callback.from_user.id
        user_info = db_manager.get_user_position(user_id)
        return user_info

    async def get_fullname_msg(self, message):
        user_id = message.from_user.id
        fullname = db_manager.get_fullname(user_id)
        print(fullname)
        return fullname

