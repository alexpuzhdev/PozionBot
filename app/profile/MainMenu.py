import os

from aiogram import Bot, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
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
delete_msg = DeleteMessage()


@MainMenu_router.message(CommandStart())
async def start(message: Message):
    date_msg = DateMessage(message)
    await delete_msg.delete_bot_msg(message)
    user_data = await userdata.user_data_message(message)
    db_manager.insert_into_users_table(user_data)
    sent_message = (await message.answer(f'Добро пожаловать, <b>@{message.from_user.username}</b>',
                                         reply_markup=kb.main, parse_mode='HTML')).message_id
    await date_msg.append_message(sent_message)


@MainMenu_router.callback_query(F.data == 'main_menu')
async def main_menu(callback: CallbackQuery):
    date_msg = DateMessage(callback)
    await callback.message.delete()
    user_data = await userdata.user_data_message(callback)
    db_manager.insert_into_users_table(user_data)
    sent_message = (await callback.message.answer(f'Добро пожаловать, <b>@{callback.from_user.username}</b>',
                                                  reply_markup=kb.main, parse_mode='HTML')).message_id
    await date_msg.append_message(sent_message)
