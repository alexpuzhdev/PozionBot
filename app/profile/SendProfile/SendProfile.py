from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from dotenv import load_dotenv
import os
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.DateMessage.DateMessage import DateMessage
from app.profile.service.get_info.GetUserPosition import GetUserPosition
from app.profile.service.checks.Avatar import Avatar
from app.profile.service.templates_profile.TemplateAdmin import TemplateAdmin
from app.profile.service.templates_profile.TemplateManager import TemplateManager
from app.profile.service.templates_profile.TemplateUser import TemplateUser
from app.profile.user.keyboards import ProfileKeyboards as kb_user
from app.profile.admin.keyboards import ProfileKeyboards as kb_admin
from app.profile.manager.keyboards import ProfileKeyboards as kb_manager

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
db_manager = DatabaseManager('Database.sqlite')

user_pos = GetUserPosition()


class SendProfile:
    def __init__(self):
        self.position = None
        self.avatar = Avatar()
        self.caption_user = TemplateUser()
        self.caption_manager = TemplateManager()
        self.caption_admin = TemplateAdmin()
        self.kb_user = kb_user.profile_user
        self.kb_admin = kb_admin.profile_admin
        self.kb_manager = kb_manager.profile_manager

    async def send_profile_msg(self, message):
        """Метод если пользователь отправил сообщение"""

        user_position = await user_pos.get_user_position_msg(message)
        profile_messages = {
            'Пользователь': self.send_user_profile_msg,
            'Админ': self.send_admin_profile_msg,
            'Менеджер': self.send_manager_profile_msg,
            'Байер': self.send_buyer_profile_msg
        }
        send_profile_func = profile_messages.get(user_position, self.send_unknown_profile_msg)
        self.position = user_position
        await send_profile_func(message)

    async def send_user_profile_msg(self, message):
        date_msg = DateMessage(message)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        photo = await self.avatar.check_avatar_msg(message)
        caption = await self.caption_user.get_caption(message)
        sent_message = (await message.answer_photo(photo=photo, caption=f'{caption}', parse_mode='HTML',
                                                   reply_markup=self.kb_user)).message_id
        await date_msg.append_message(sent_message)

    async def send_manager_profile_msg(self, message):
        date_msg = DateMessage(message)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        photo = await self.avatar.check_avatar_msg(message)
        caption = await self.caption_manager.get_caption(message)
        sent_message = (await message.answer_photo(photo=photo, caption=f'{caption}', parse_mode='HTML',
                                                   reply_markup=self.kb_manager)).message_id
        await date_msg.append_message(sent_message)

    async def send_admin_profile_msg(self, message):
        date_msg = DateMessage(message)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        photo = await self.avatar.check_avatar_msg(message)
        caption = await self.caption_admin.get_caption(message)
        sent_message = (await message.answer_photo(photo=photo, caption=f'{caption}', parse_mode='HTML',
                                                   reply_markup=self.kb_admin)).message_id
        await date_msg.append_message(sent_message)

    async def send_buyer_profile_msg(self, message):
        date_msg = DateMessage(message)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        photo = await self.avatar.check_avatar_msg(message)
        sent_message = (await message.answer_photo(photo=photo, caption=f'Вы {self.position}')).message_id
        await date_msg.append_message(sent_message)

    async def send_unknown_profile_msg(self, message):
        date_msg = DateMessage(message)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        photo = await self.avatar.check_avatar_msg(message)
        sent_message = (await message.answer_photo(photo=photo,
                                                   caption=f'Вы не зарегистрированы, пожалуйста пройдите регистрацию'
                                                   )).message_id
        await date_msg.append_message(sent_message)

    async def send_profile_clb(self, callback):
        """Метод если пользователь отправил колбек"""

        user_position = await user_pos.get_user_position_msg(callback)
        profile_messages = {
            'Пользователь': self.send_user_profile_clb,
            'Админ': self.send_admin_profile_clb,
            'Менеджер': self.send_manager_profile_clb,
            'Байер': self.send_buyer_profile_clb
        }
        send_profile_func_clb = profile_messages.get(user_position, self.send_unknown_profile_msg)
        self.position = user_position
        await send_profile_func_clb(callback)

    async def send_user_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_clb(callback)
        caption = await self.caption_user.get_caption(callback)
        await callback.message.answer_photo(photo=photo, caption=f'{caption}', parse_mode='HTML',
                                            reply_markup=self.kb_user)

    async def send_admin_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_clb(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_manager_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_clb(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_buyer_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_clb(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы {self.position}')

    async def send_unknown_profile_clb(self, callback):
        photo = await self.avatar.check_avatar_clb(callback)
        await callback.answer_photo(photo=photo, caption=f'Вы не зарегистрированы, пожалуйста пройдите регистрацию')
