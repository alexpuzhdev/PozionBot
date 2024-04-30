import os

from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv

from app.profile.keyboard_main_menu import keyboards as kb

MainMenu_router = Router()

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()


@MainMenu_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Добро пожаловать, <b>@{message.from_user.username}</b>',
                         reply_markup=kb.main, parse_mode='HTML')
