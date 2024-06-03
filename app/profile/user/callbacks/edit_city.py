import os

from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from app.profile.SendProfile.SendProfile import SendProfile
from app.Database.DataBaseManager import DatabaseManager
from app.profile.service.DateMessage.DateMessage import DateMessage
from app.profile.service.Deleter.Deleter import DeleteMessage, DeleteCallback
from app.profile.user.keyboards import edit_city as kb
from app.profile.user.FSM.edit_city import EditCity

EditCity_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()
deleter_msg = DeleteMessage()
deleter_clb = DeleteCallback()


@EditCity_router.callback_query(F.data == 'edit_city')
async def edit_info(callback: CallbackQuery, state: FSMContext):
    date_msg = DateMessage(message=callback)
    await callback.message.delete()
    sent_message = (
        await callback.message.answer('Введите ваш город')).message_id
    await state.set_state(EditCity.city)
    await date_msg.append_message(sent_message)


@EditCity_router.message(F.text, EditCity.city)
async def edit_info(message: Message, state: FSMContext):
    date_msg = DateMessage(message)
    await state.update_data(user_id=message.from_user.id)
    await state.update_data(city=message.text)
    data = await state.get_data()
    print(f"{data['city']}")
    await deleter_msg.delete_all_msg(message)
    sent_message = (
        await message.answer(f"Ваш город: {data['city']}", reply_markup=kb.fsm_city)).message_id
    await date_msg.append_message(sent_message)


@EditCity_router.callback_query(F.data == 'complete_city')
async def edit_info(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Ваши данные успешно обновлены', show_alert=True)
    data = await state.get_data()
    await deleter_msg.delete_all_msg(callback)
    db_manager.insert_city(data)
    await send_profile.send_profile_clb(callback)
