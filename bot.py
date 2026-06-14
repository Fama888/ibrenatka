import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k"

if not TOKEN:
    raise Exception("TOKEN not found")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Каталог", callback_data="catalog")]
    ])
    await message.answer("Привет 👋", reply_markup=kb)

@dp.callback_query(F.data == "catalog")
async def catalog(call):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📸 Фото", callback_data="photo")],
        [InlineKeyboardButton(text="🎥 Видео", callback_data="video")]
    ])
    await call.message.answer("Выбери категорию 👇", reply_markup=kb)

@dp.callback_query(F.data == "photo")
async def photo(call):
    await call.message.answer("📸 Фото каталог (пока пусто)")

@dp.callback_query(F.data == "video")
async def video(call):
    await call.message.answer("🎥 Видео каталог (пока пусто)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
