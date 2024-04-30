import os
from aiogram import Bot
from dotenv import load_dotenv

from app.profile.service.checks.CheckFullName import CheckFullName
from app.profile.service.checks.GetUserInfo import GetUserInfo

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


class TemplateUser:
    def __init__(self):
        self.user_info_service = GetUserInfo()
        self.current_fullname = CheckFullName()

    async def get_user_info(self, message):
        user_info = await self.user_info_service.get_user_info_msg(message)
        return user_info

    async def get_caption(self, message):
        user_info = await self.get_user_info(message)
        id = user_info[0]
        user_id = user_info[1]
        first_name_tg = user_info[2]
        last_name_tg = user_info[3]
        user_name_tg = user_info[4]
        user_position = user_info[5]
        count_orders = user_info[6]
        city = user_info[7]
        address = user_info[8]
        firstname = user_info[9]
        surname = user_info[10]
        lastname = user_info[11]
        phone_number = user_info[12]
        active_delivery = user_info[13]
        pers_loyalty = user_info[14]
        pers_referal_link = user_info[15]
        from_referal_link = user_info[16]
        full_name = await self.current_fullname.get_correct_fullname_msg(message)
        if full_name == 'Не указан Не указано Не указано':
            full_name = 'Не указано'

        caption_text = (f'Мой профиль: <b>@{user_name_tg}</b>\n\n'
                        f'Категория: <b>{user_position}</b>\n'
                        f'Количество заказов: <b>{count_orders}</b>\n\n'
                        f'ФИО: <b>{full_name}</b> \n'
                        f'Город: <b>{city}</b>\n'
                        f'Адрес: <b>{address}</b>\n'
                        f'Номер телефона: <b>{phone_number}</b>\n\n'
                        f'Активная доставка: <b>{active_delivery}</b>\n'
                        f'Персональная скидка: <b>{pers_loyalty}</b>\n\n'
                        f'Реферальная ссылка для друзей:\n<b>{pers_referal_link}</b>\n\n')
        if from_referal_link is not None:
            caption_text += f'Вас пригласил: {from_referal_link}'
        return caption_text

