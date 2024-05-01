import os
from aiogram import Bot
from dotenv import load_dotenv
from app.profile.service.get_info.GetUserInfo import GetUserInfo

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


class CheckFullName:
    def __init__(self):
        self.user_info = GetUserInfo()
        self.fullname = list()
        self.correct_fullname = []

    async def get_fullname_msg(self, message):
        self.fullname = await self.user_info.get_fullname_msg(message)
        return self.fullname

    async def get_correct_fullname_msg2(self, message):
        self.fullname = await self.get_fullname_msg(message)
        return self.fullname[0]

    async def get_correct_fullname_msg(self, message):
        self.fullname = await self.get_fullname_msg(message)
        firstname, surname, lastname = self.fullname

        if firstname == 'Не указано' and surname == 'Не указано' and lastname == 'Не указано':
            return 'Не указано'
        else:
            parts = []
            if firstname != 'Не указано':
                parts.append(firstname)
            if surname != 'Не указано':
                parts.append(surname)
            if lastname != 'Не указано':
                parts.append(lastname)

            if len(parts) == 0:
                return '(Фамилия и отчество не указаны)'
            else:
                result = ' '.join(parts)
                if len(parts) == 1:
                    result += ' (Фамилия и отчество не указаны)'
                else:
                    if firstname == 'Не указано':
                        result += ' (Имя не указано)'
                    if surname == 'Не указано':
                        result += ' (Отчество не указана)'
                    if lastname == 'Не указано':
                        result += ' (Фамилия не указана)'

                    # Добавлено условие для вывода, если указаны имя и отчество
                    if firstname != 'Не указано' and lastname != 'Не указано' and surname == 'Не указано':
                        result += ' (Фамилия не указана)'

                return result