import os
from aiogram import Bot
from dotenv import load_dotenv

from app.profile.service.checks.CheckFullName import CheckFullName
from app.profile.service.get_info.GetManagerInfo import GetManagerInfo

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


class TemplateManager:
    def __init__(self):
        self.manager_info = GetManagerInfo()
        self.current_fullname = CheckFullName()

    async def get_manager_info(self, message):
        manager_info_data = await self.manager_info.get_manager_info_msg(message)
        return manager_info_data

    async def get_caption(self, message):
        manager_info_data = await self.get_manager_info(message)
        id = manager_info_data[0]
        user_id = manager_info_data[1]
        firstname = manager_info_data[2]
        lastname = manager_info_data[3]
        username = manager_info_data[4]
        ticket_count = manager_info_data[5]
        open_ticket_count = manager_info_data[6]
        caption_text = (f'Мой профиль: <b>@{username}</b>\n\n'
                        f'Категория: <b>Менеджер</b>\n\n'
                        f'Всего обращений: {ticket_count}\n'
                        f'Отрытых обращений: {open_ticket_count}\n')
        return caption_text

