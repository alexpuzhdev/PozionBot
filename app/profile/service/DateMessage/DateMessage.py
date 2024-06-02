from app.profile.service.Deleter.Deleter import date_messages


class DateMessage:
    @staticmethod
    async def user_id(message):
        return message.from_user.id

    @staticmethod
    async def append_message(message, sent_message):
        user_id = await DateMessage.user_id(message)
        if user_id not in date_messages:
            date_messages[user_id] = []
        date_messages[user_id].append(sent_message)
        print("Сообщение успешно добавлено в список для данного пользователя")
        print(date_messages)
