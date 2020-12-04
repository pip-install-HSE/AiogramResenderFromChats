import logging

from aiogram import Bot, Dispatcher, executor # aiogram lib
from aiogram import types
from aiogram.contrib.fsm_storage.mongo import MongoStorage # storage to save user's state
from aiogram.contrib.middlewares.logging import LoggingMiddleware # logger

from config import *
from database import Database

# Configure logging
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-4s [%(asctime)s]  %(message)s', level=logging.INFO)

logger = logging.getLogger()

formatter = logging.Formatter(u'%(filename)s [LINE:%(lineno)d] #%(levelname)-4s [%(asctime)s]  %(message)s')

file_handler = logging.FileHandler("logs/bot.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

error_file_handle = logging.FileHandler("logs/bot_errors.log")
error_file_handle.setLevel(logging.ERROR)
error_file_handle.setFormatter(formatter)

logger.addHandler(error_file_handle)
logger.addHandler(file_handler)

# Initialize databse
db = Database()

# Initialize bot, storage and dispatcher
storage = MongoStorage(host=MONGO_HOST, port=MONGO_PORT, db_name='aiogram_fsm')
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())