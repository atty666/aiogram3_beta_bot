import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from tokens import bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello my sweet friend!')


@dp.message()
async def wrong_cmd(message: types.Message):
    await message.answer('Wrong command!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
