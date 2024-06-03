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

