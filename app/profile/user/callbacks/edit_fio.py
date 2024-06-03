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
from app.profile.user.FSM.edit_fio.EditFio import EditFio
from app.profile.user.keyboards import edit_info as kb
from app.profile.user.FSM.edit_fio.edit_fio import FSMEditFio

EditUserProfile_router = Router()
db_manager = DatabaseManager('Database.sqlite')
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()

send_profile = SendProfile()
deleter_msg = DeleteMessage()
deleter_clb = DeleteCallback()


@EditUserProfile_router.callback_query(F.data == 'edit_info')
async def edit_info(callback: CallbackQuery):
    date_msg = DateMessage(message=callback)
    await callback.message.delete()
    sent_message = (
        await callback.message.answer('Выберите данные для редактирования', reply_markup=kb.edit_kb)).message_id
    await date_msg.append_message(sent_message)


@EditUserProfile_router.callback_query(F.data == 'edit_fio')
async def edit_fio(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    edit_fio = EditFio(data)
    await callback.message.delete()
    await callback.message.answer(edit_fio.get_fio_msg(
        user_id=callback.from_user.id),
        reply_markup=kb.fsm_fio,
        parse_mode='HTML')

# async def check_fio(message: Message, state: FSMContext):
#     date_msg = DateMessage(message)
#     data = await state.get_data()
#     sent_message = (
#         await message.answer(f"Давайте перепроверим данные:\n\n"
#                              f"Имя: <b>{data['firstname']}</b>\n"
#                              f"Отчество: <b>{data['thirdname']}</b>\n"
#                              f"Фамилия: <b>{data['lastname']}</b>", reply_markup=kb.fsm_fio,
#                              parse_mode='HTML')).message_id
#     await date_msg.append_message(sent_message)
#

# @EditUserProfile_router.callback_query(F.data == 'edit_fio')
# async def edit_fio(callback: CallbackQuery, state: FSMContext):
#     date_msg = DateMessage(message=callback)
#     await callback.message.delete()
#     sent_message = (
#         await callback.message.answer('Введите ваше имя')).message_id
#     await date_msg.append_message(sent_message)
#     await state.set_state(FSMEditFio.firstname)
#
#
# @EditUserProfile_router.message(F.text, FSMEditFio.firstname)
# async def firstname(message: Message, state: FSMContext):
#     date_msg = DateMessage(message)
#     await state.update_data(firstname=message.text)
#     await deleter_msg.delete_all_msg(message)
#     data = await state.get_data()
#     print(data['firstname'])
#     sent_message = (await message.answer('Введите вашу фамилию')).message_id
#     await date_msg.append_message(sent_message)
#     await state.set_state(FSMEditFio.lastname)
#
#
# @EditUserProfile_router.message(F.text, FSMEditFio.lastname)
# async def lastname(message: Message, state: FSMContext):
#     date_msg = DateMessage(message)
#     await state.update_data(lastname=message.text)
#     await deleter_msg.delete_all_msg(message)
#     data = await state.get_data()
#     print(data['lastname'])
#     sent_message = (await message.answer('Введите вашe отчество')).message_id
#     await date_msg.append_message(sent_message)
#     await state.set_state(FSMEditFio.thirdname)
#
#
# @EditUserProfile_router.message(F.text, FSMEditFio.thirdname)
# async def send_name(message: Message, state: FSMContext):
#     await state.update_data(user_id=message.from_user.id)
#     await state.update_data(thirdname=message.text)
#     await deleter_msg.delete_all_msg(message)
#     await check_fio(message, state)
#
#
# @EditUserProfile_router.callback_query(F.data == 'complete_fio')
# async def complete_fio(callback: CallbackQuery, state: FSMContext):
#     await callback.answer('Ваши данные успешно обновлены', show_alert=True)
#     data = await state.get_data()
#     db_manager.insert_fio(data)
#     await callback.message.delete()
#     await deleter_msg.delete_all_msg(callback)
#     await send_profile.send_profile_clb(callback)
#
#
# @EditUserProfile_router.callback_query(F.data == 'edit_firstname')
# async def edit_firstname(callback: CallbackQuery):
#     date_msg = DateMessage(callback)
#     await deleter_msg.delete_all_msg(callback)
#     sent_message = (await callback.message.answer('Введите ваше имя')).message_id
#     await date_msg.append_message(sent_message)
#
#
# @EditUserProfile_router.message(F.text)
# async def edit_firstname(message: Message, state: FSMContext):
#     await state.update_data(firstname=message.text)
#     await deleter_msg.delete_all_msg(message)
#     data = await state.get_data()
#     sent_message = (await message.answer(f"Давайте перепроверим данные:\n\n"
#                                          f"Имя: <b>{data['firstname']}</b>\n"
#                                          f"Отчество: <b>{data['thirdname']}</b>\n"
#                                          f"Фамилия: <b>{data['lastname']}</b>", reply_markup=kb.fsm_fio,
#                                          parse_mode='HTML')).message_id
#     print(f"Имя: {data['firstname']}, Фамилия:{data['lastname']},"
#           f" Отчество: {data['thridname']}, user_id: {data['user_id']}")
