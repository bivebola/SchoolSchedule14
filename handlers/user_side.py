from aiogram import types
from create_bot import bot,dp
from handlers.states import NewsStates
from aiogram.dispatcher import FSMContext
from data_base import sqlite_db
from keyboards import inline_kb, delete_kb
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id,'Привет! Я бот с расписанием! Помощь по командам /help')

@dp.message_handler(commands=['news', 'новости'])
async def news_command(message: types.Message):
    news = await sqlite_db.get_news()
    for i in news[:3]:
        await bot.send_photo(message.chat.id, i[3], f'*{i[1]}*\n\n{i[2]}',
                             parse_mode='Markdown')