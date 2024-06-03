from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
date_messages = {}


class DeleteMessage:
    @staticmethod
    async def delete_bot_msg(message):
        user_id = message.from_user.id
        if user_id in date_messages:
            for message_id in date_messages[user_id]:
                try:
                    await bot.delete_message(message_id=message_id, chat_id=user_id)
                except Exception as e:
                    print(f"Ошибка при удалении сообщения {message_id}: {e}")
            date_messages[user_id].clear()
        else:
            print("Пользователь не имеет сообщений для удаления")

    @staticmethod
    async def delete_user_msg(message):
        user_id = message.from_user.id
        message_id = message.message_id
        try:
            await bot.delete_message(message_id=message_id, chat_id=user_id)
        except Exception as e:
            print(f"Ошибка при удалении сообщения {message_id}: {e}")

    @staticmethod
    async def delete_all_msg(message):
        try:
            await DeleteMessage.delete_user_msg(message)
        except Exception as e:
            print(f"Ошибка при удалении сообщения: {e}")
        try:
            await DeleteMessage.delete_bot_msg(message)
        except Exception as e:
            print(f"Ошибка при удалении коллбека: {e}")



class DeleteCallback:
    @staticmethod
    async def delete_bot_msg(callback_query):
        user_id = callback_query.from_user.id
        if user_id in date_messages:
            for message_id in date_messages[user_id]:
                try:
                    await bot.delete_message(message_id=message_id, chat_id=user_id)
                except Exception as e:
                    print(f"Ошибка при удалении сообщения {message_id}: {e}")
            date_messages[user_id].clear()
        else:
            print("Пользователь не имеет сообщений для удаления")

    @staticmethod
    async def delete_user_msg(callback_query):
        user_id = callback_query.from_user.id
        message_id = callback_query.message_id
        try:
            await bot.delete_message(message_id=message_id, chat_id=user_id)
        except Exception as e:
            print(f"Ошибка при удалении сообщения {message_id}: {e}")
