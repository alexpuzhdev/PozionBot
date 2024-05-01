import os
from aiogram import Bot
from dotenv import load_dotenv

from app.profile.service.checks.CheckFullName import CheckFullName
from app.profile.service.get_info.GetAdminInfo import GetAdminInfo

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


class TemplateAdmin:
    def __init__(self):
        self.admin_info = GetAdminInfo()
        self.current_fullname = CheckFullName()

    async def get_admin_info(self, message):
        admin_info_data = await self.admin_info.get_admin_info_msg(message)
        return admin_info_data

    async def get_caption(self, message):
        admin_info_data = await self.get_admin_info(message)
        id = admin_info_data[0]
        user_id = admin_info_data[1]
        firstname = admin_info_data[2]
        lastname = admin_info_data[3]
        username = admin_info_data[4]
        count_users = admin_info_data[5]
        count_pers = admin_info_data[6]
        caption_text = (f'Мой профиль: <b>@{username}</b>\n\n'
                        f'Категория: <b>Админ</b>\n\n'
                        f'Количество пользователей в боте: <b>{count_users}</b>\n'
                        f'Количество персонала: <b>{count_pers}</b>\n')
        return caption_text

