import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import start
from handlers import weather
from config_reader import config

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(start.router)
    dp.include_router(weather.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
