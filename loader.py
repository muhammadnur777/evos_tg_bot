import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database.db_sqlite import Database

API_TOKEN = '6474886692:AAFSZ6EdlRSUcSfitTwfXmLL_67DEOGq9Do'

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=API_TOKEN, parse_mode = ParseMode.HTML)

dp = Dispatcher(bot, storage=storage)
db = Database('main.sqlite3')
