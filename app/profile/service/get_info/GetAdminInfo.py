from aiogram import Bot

from dotenv import load_dotenv
import os
from app.Database.DataBaseManager import DatabaseManager

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
db_manager = DatabaseManager('Database.sqlite')


class GetAdminInfo:

    async def get_admin_info_msg(self, message):
        user_id = message.from_user.id
        admin_info = db_manager.get_info_for_admin(user_id)
        return admin_info

    async def get_admin_info_clb(self, callback):
        user_id = callback.from_user.id
        admin_info = db_manager.get_info_for_admin(user_id)
        return admin_info

    async def get_admin_position_msg(self, message):
        user_id = message.from_user.id
        user_position = db_manager.get_user_position(user_id)
        return user_position

    async def get_admin_position_clb(self, callback):
        user_id = callback.from_user.id
        user_info = db_manager.get_user_position(user_id)
        return user_info

    async def get_fullname_msg(self, message):
        user_id = message.from_user.id
        fullname = db_manager.get_fullname(user_id)
        print(fullname)
        return fullname
