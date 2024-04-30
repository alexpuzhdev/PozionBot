import os
from aiogram import Bot

bot = Bot(os.getenv('TOKEN'))


class Avatar:
    def __init__(self):
        self.base_photo = ('https://sneg.top/uploads/posts/2023-04/1680702072'
                           '_sneg-top-p-kartinki-dlya-feisita-instagram-36.jpg')

    async def check_avatar_msg(self, message):
        try:
            avatar = await bot.get_user_profile_photos(message.from_user.id)
            return avatar.photos[0][0].file_id if avatar else self.base_photo
        except Exception as e:
            print(f"An error occurred while getting user's avatar: {e}")
            return self.base_photo

    async def check_avatar_clb(self, callback):
        try:
            avatar = await bot.get_user_profile_photos(callback.from_user.id)
            return avatar.photos[0][0].file_id if avatar else self.base_photo
        except Exception as e:
            print(f"An error occurred while getting user's avatar: {e}")
            return self.base_photo
