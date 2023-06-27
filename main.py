import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
