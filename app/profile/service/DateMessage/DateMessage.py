from app.profile.service.Deleter.Deleter import date_messages


# class DateMessage:
#     @staticmethod
#     async def user_id(message):
#         print(message.from_user.id)
#         return message.from_user.id
#
#     @staticmethod
#     async def append_message(message, sent_message):
#         user_id = await DateMessage.user_id(message)
#         if user_id not in date_messages:
#             date_messages[user_id] = []
#         try:
#             date_messages[user_id].append(sent_message)
#             print("Сообщение успешно добавлено в список для данного пользователя")
#             print(date_messages)
#         except Exception as e:
#             print(f"Ошибка при добавлении сообщения в date_message: {e}")


class DateMessage:
    def __init__(self, message):
        self.user_id = message.from_user.id

    async def append_message(self, sent_message):
        user_id = self.user_id
        if user_id not in date_messages:
            date_messages[user_id] = []
        try:
            date_messages[user_id].append(sent_message)
            print("Сообщение успешно добавлено в список для данного пользователя")
            print(date_messages)
        except Exception as e:
            print(f"Ошибка при добавлении сообщения в date_message: {e}")
