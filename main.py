from aiogram import executor
from handlers import cart_handler, start_handler, user_handler

from loader import dp


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




 