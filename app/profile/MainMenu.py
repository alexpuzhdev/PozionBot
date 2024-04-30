import os

from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv

from app.profile.service.checks.UserPosition import UserPosition
from app.profile.service.keyboards import MainMenuKeyboard as kb
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.UserData.UserData import UserData

MainMenu_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

userdata = UserData()


@MainMenu_router.message(CommandStart())
async def start(message: Message):
    user_data = await userdata.user_data_message(message)
    db_manager.insert_into_users_table(user_data)
    await message.answer(f'Добро пожаловать, <b>@{message.from_user.username}</b>',
                         reply_markup=kb.main, parse_mode='HTML')
