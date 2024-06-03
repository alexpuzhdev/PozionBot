import os

from aiogram import Bot, Router
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from app.profile.SendProfile.SendProfile import SendProfile
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.Deleter.Deleter import DeleteMessage, DeleteCallback

EditUserProfile_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()
deleter_msg = DeleteMessage()
deleter_clb = DeleteCallback()


class EditFio:
    def __init__(self, data):
        self.data = data

    def get_fio_msg(self, user_id):
        firstname = db_manager.get_firstname(user_id)
        surname = db_manager.get_surname(user_id)
        lastname = db_manager.get_lastname(user_id)

        caption = (f"Вот, что нам известно:\n\n"
                   f"Имя: <b>{firstname}</b>\n"
                   f"Отчество: <b>{surname}</b>\n"
                   f"Фамилия: <b>{lastname}</b>")
        return caption