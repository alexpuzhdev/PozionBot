import os

from aiogram import Bot, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from app.profile.SendProfile.SendProfile import SendProfile
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.Deleter.Deleter import DeleteMessage, DeleteCallback

UserProfile_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()
deleter_msg = DeleteMessage()
deleter_clb = DeleteCallback()


@UserProfile_router.message(F.text == 'Профиль')
async def get_profile(message: Message):
    await deleter_msg.delete_bot_msg(message)
    await send_profile.send_profile_msg(message)


@UserProfile_router.callback_query(F.data == 'Профиль')
async def get_profile(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await deleter_msg.delete_bot_msg(callback)
    await send_profile.send_profile_clb(callback)
