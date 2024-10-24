#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from FormaAdmin import *
from keyboard import*
from database import*
from config import*
from Forma import*
import asyncio
from traits import*
import time
from FormaAdmin import*



generator = Generator()
btn = Button()
db = Database()

@dp.message_handler(commands=['start', 'go'])
async def start_handler(message: types.Message):
    print(message.from_user.id)
      
    #from datetime import datetime
    #fileId = "AgACAgIAAxkBAANcZwwL-emYUtwEKC8tOLtMa93tOnMAAqfoMRtMEGBILbrCi2y-dy4BAAMCAAN5AAM2BA"

    #user_id = message.from_user.id
    #user_name = f"@{message.from_user.username}"
    #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #db.JustInsert(user_id, user_name, time_now)  
    
    await bot.send_message(
        message.from_user.id,
        text="""Добро пожаловать в FavPlaces! Здесь вы можете добавлять заведения и получать баллы для скидочной карты. Введите команду или используйте меню для действий.""",
        parse_mode="Markdown",
        reply_markup=btn.menu()
    )

@dp.message_handler(commands=['admin'])
async def handler(message: types.Message):
    print(message.from_user.id)
    if message.from_user.id == admin or message.from_user.id == admin2 or message.from_user.id == admin3:
        await bot.send_message(
        message.from_user.id,
        text="😊 *Сәлеметсіз бе %s !\nСіздің статусыңыз 👤 Админ(-ка-)*"%message.from_user.first_name,
        parse_mode="Markdown",
        reply_markup=btn.admin()
    )

@dp.callback_query_handler()
async def callback_inline(call: types.CallbackQuery):
    if call.data.startswith("accept_establishment:"):
        establishment_id = call.data.split(":")[1]
        if establishment_id in Establishments:
            est_data = Establishments.pop(establishment_id)
            # Отправляем сообщение пользователю об одобрении
            await bot.send_message(est_data['user_id'], "Ваше заведение было одобрено!")
            # Уведомляем администратора
            await bot.send_message(call.message.chat.id, f"Заведение '{est_data['data']}' одобрено!")
        else:
            await bot.send_message(call.message.chat.id, "Информация о заведении не найдена.")
    elif call.data.startswith("reject_establishment:"):
        establishment_id = call.data.split(":")[1]
        if establishment_id in Establishments:
            est_data = Establishments.pop(establishment_id)
            # Отправляем сообщение пользователю об отклонении
            await bot.send_message(est_data['user_id'], "К сожалению, ваше заведение было отклонено.")
            # Уведомляем администратора
            await bot.send_message(call.message.chat.id, f"Заведение '{est_data['data']}' отклонено.")
        else:
            await bot.send_message(call.message.chat.id, "Информация о заведении не найдена.")


# 🖊 Добавить заведение
@dp.message_handler(commands=['add'])
@dp.message_handler(Text(equals="🖊 Добавить заведение"), content_types=['text'])
async def handler(message: types.Message):

    await Forma.s1.set()

    await bot.send_message(
        message.from_user.id,
        text="""*Введите название заведения, которое вы хотите добавить*""",
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )

# 🔍 Посмотреть мои заведения
@dp.message_handler(commands=['look'])
@dp.message_handler(Text(equals="🔍 Посмотреть мои заведения"), content_types=['text'])
async def handler(message: types.Message):


    await bot.send_message(
        message.from_user.id,
        text="""*Введите название заведения, которое вы хотите добавить*""",
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )

# 🧮 Проверить баллы и скидочную карту
@dp.message_handler(commands=['search'])
@dp.message_handler(Text(equals="🧮 Проверить баллы и скидочную карту"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*У вас X баллов. Добавьте еще Y заведений для получения скидочной карты.*""",
        parse_mode="Markdown",
        reply_markup=btn.sale()
    )


# 👤 Профиль
@dp.message_handler(commands=['profile'])
@dp.message_handler(Text(equals="👤 Профиль"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*Ваше имя: %s*"""%message.from_user.first_name,
        parse_mode="Markdown"
    )


# Admins
# ✔️ Одобрить заведения
@dp.message_handler(Text(equals="✔️ Одобрить заведения"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*Введите название заведения, которое вы хотите добавить*""",
        parse_mode="Markdown",
        reply_markup=btn.admin()
    )

# 🔴 Отклонить заведения
@dp.message_handler(Text(equals="🔴 Отклонить заведения"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*Введите название заведения, которое вы хотите добавить*""",
        parse_mode="Markdown",
        reply_markup=btn.admin()
    )

# 🗂 Просмотреть список ожидающих заведений
@dp.message_handler(Text(equals="🗂 Просмотреть список ожидающих заведений"), content_types=['text'])
async def handler(message: types.Message):

    await bot.send_message(
        message.from_user.id,
        text="""*Введите название заведения, которое вы хотите добавить*""",
        parse_mode="Markdown",
        reply_markup=btn.admin()
    )

