from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6246684168:AAEhw34uNm_SL5yUYTq06VuzQ7ZMtjusIvg')

dp = Dispatcher(bot, storage=storage)