import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from root import TOKEN

from db import Database

db = Database("preson.db")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello there!")
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
    else:
        await message.answer("siz avval ham botga start boshgansiz")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
