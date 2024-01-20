import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from root import TOKEN
import sqlite3

DATABASE_FILE = 'user_db.sqlite'

conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(255),
        username VARCHAR(255),
        user_id INTEGER
    )
''')
conn.commit()


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello there!")
    cursor.execute('INSERT INTO messages (full_name, username, user_id) VALUES (?, ?, ?)',
                   (message.from_user.full_name, message.from_user.username, message.from_user.id))
    conn.commit()
    await message.answer("send your telegram data")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
