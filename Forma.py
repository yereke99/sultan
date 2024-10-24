from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import Message
from load import dp, bot
from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import logging
from keyboard import*
from database import Database
import datetime
from main import*
import asyncio
from config import admin
from datetime import datetime
from traits import *
import time
from traits import*
from config import*
import os
import uuid


generator = Generator()
btn = Button()
db = Database()




# Хранилище заведений (глобальная переменная или используйте базу данных)
Establishments = {}

class Forma(StatesGroup):
    s1 = State()  
    

@dp.message_handler(state='*', commands='🔕 Отмены операции')
@dp.message_handler(Text(equals='🔕 Отмены операции', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
    :param message: Бастартылды
    :param state: Тоқтату
    :return: finish
    """
    
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Бас тарту!')
    
    await state.finish()
    await message.reply('Сіз тапсырыстан бас тарттыңыз.', reply_markup=btn.menu_not_paid())

@dp.message_handler(state=Forma.s1)
async def send_to_users(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['data'] = message.text
        data['user_name'] = message.from_user.username or "No username"
        data['user_id'] = message.from_user.id

    establishment_id = str(uuid.uuid4()) 
    Establishments[establishment_id] = dict(data)  # Преобразование в словарь
    
    await bot.send_message(
        message.from_user.id,
        text="Заведение отправлено на модерацию. Вы получите уведомление, когда оно будет одобрено.",
        reply_markup=btn.menu()
    )

    # Отправляем сообщение администратору с уникальными кнопками
    await bot.send_message(
        admin,
        text=f"Заведение: {data['data']}\nЮзер: {data['user_name']}",
        reply_markup=btn.accept(establishment_id)
    )

    await state.finish()
