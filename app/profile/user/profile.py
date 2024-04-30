import os

from aiogram import Bot, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv

from app.profile.service.SendProfile import SendProfile
from app.profile.service.checks.UserPosition import UserPosition
from app.profile.service.keyboards import MainMenuKeyboard as kb
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.UserData.UserData import UserData
from app.profile.service.checks.GetUserInfo import GetUserInfo


UserProfile_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()


@UserProfile_router.message(F.text == 'Профиль')
async def get_profile(message: Message):
    await send_profile.send_profile_msg(message)
