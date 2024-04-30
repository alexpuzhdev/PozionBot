import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

from app.Database.DataBaseManager import DatabaseManager
from app.profile.MainMenu import MainMenu_router


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

""" Создание экземпляра Dispatcher """
dp = Dispatcher(storage=storage)

""" Включаем логирование, чтобы не пропустить важные сообщения """

logging.basicConfig(level=logging.INFO)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    db_manager = DatabaseManager('Database.sqlite')
    db_manager.create_users_table()
    dp.include_routers(
        MainMenu_router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())