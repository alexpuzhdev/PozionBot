import os

from aiogram import Bot, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from app.profile.SendProfile.SendProfile import SendProfile
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.DateMessage.DateMessage import DateMessage
from app.profile.service.Deleter.Deleter import DeleteMessage, DeleteCallback

EditUserProfile_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()
deleter_msg = DeleteMessage()
deleter_clb = DeleteCallback()
date_msg = DateMessage()


@EditUserProfile_router.callback_query(F.data == 'edit_info')
async def get_profile(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Редактирование профиля')
