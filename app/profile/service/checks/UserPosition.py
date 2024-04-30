from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
import os
from app.Database.DataBaseManager import DatabaseManager

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
db_manager = DatabaseManager('Database.sqlite')


class UserPosition:

    async def get_user_position_msg(self, message):
        user_id = message.from_user.id
        user_position = db_manager.get_user_position(user_id)
        return user_position

    async def get_user_position_clb(self, callback):
        user_id = callback.from_user.id
        user_position = db_manager.get_user_position(user_id)
        return user_position