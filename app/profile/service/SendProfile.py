from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
import os
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.checks.UserPosition import UserPosition
from app.profile.service.checks.Avatar import Avatar
from app.profile.service.templates_profile.TemplateUser import TemplateUser

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
db_manager = DatabaseManager('Database.sqlite')

user_pos = UserPosition()


class SendProfile:
    def __init__(self):
        self.position = user_pos
        self.avatar = Avatar()
        self.caption = TemplateUser()

    async def send_profile_msg(self, message):
        """Метод если пользователь отправил сообщение"""

        user_position = await user_pos.get_user_position_msg(message)
        profile_messages = {
            'Пользователь': self.send_user_profile_msg,
            'Админ': self.send_admin_profile_msg,
            'Менеджер': self.send_manager_profile_msg,
            'Байер': self.send_buyer_profile_msg
        }
        send_profile_func = profile_messages.get(user_position)
        self.position = user_position
        await send_profile_func(message)

    async def send_user_profile_msg(self, message):
        photo = await self.avatar.check_avatar_msg(message)
        caption = await self.caption.get_caption(message)
        await message.answer_photo(photo=photo, caption=f'{caption}', parse_mode='HTML')

    async def send_admin_profile_msg(self, message):
        photo = await self.avatar.check_avatar_msg(message)
        await message.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_manager_profile_msg(self, message):
        photo = await self.avatar.check_avatar_msg(message)
        await message.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_buyer_profile_msg(self, message):
        photo = await self.avatar.check_avatar_msg(message)
        await message.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_profile_clb(self, callback):
        """Метод если пользователь отправил колбек"""

        user_position = await user_pos.get_user_position_msg(callback)
        profile_messages = {
            'Пользователь': self.send_user_profile_clb,
            'Админ': self.send_admin_profile_clb,
            'Менеджер': self.send_manager_profile_clb,
            'Байер': self.send_buyer_profile_clb
        }
        send_profile_func = profile_messages.get(user_position)
        self.position = user_position
        await send_profile_func(callback)

    async def send_user_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_msg(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_admin_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_msg(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_manager_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_msg(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_buyer_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_msg(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

