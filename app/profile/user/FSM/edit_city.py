import os

from aiogram import Bot, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State

from dotenv import load_dotenv

from app.profile.service.DateMessage.DateMessage import DateMessage
from app.profile.service.Deleter.Deleter import DeleteMessage
from app.profile.service.keyboard_main_menu import keyboards as kb
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.users_data.user import UserData

MainMenu_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

userdata = UserData()


class EditCity(StatesGroup):
    user_id = State()
    city = State()
    second = State()
    third = State()
