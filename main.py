import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from app.handlers import router
from config import TOKEN


async def main():

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
