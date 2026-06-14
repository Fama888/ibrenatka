import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# ===== TOKEN (Render ENV) =====
TOKEN = os.getenv("8635030604:AAFOUJg7nPogKWqUpzjbsbAJAyfNe8mDq6k")

if not TOKEN:
    raise Exception("TOKEN not found")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== КНОПКИ =====

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")]
    ],
    resize_keyboard=True
)

catalog_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Фото"), KeyboardButton(text="🎥 Видео")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

# ===== START =====

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет 👋\nДобро пожаловать в магазин 💜\nНажми каталог 👇",
        reply_markup=main_menu
    )

# ===== КАТАЛОГ =====

@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    await message.answer("Выбери категорию 👇", reply_markup=catalog_menu)

@dp.message(F.text == "⬅️ Назад")
async def back(message: Message):
    await message.answer("Главное меню 👇", reply_markup=main_menu)

# ===== ФОТО =====

@dp.message(F.text == "📸 Фото")
async def photos(message: Message):
    await message.answer(
        "📸 Фото товары:\n\n"
        "1. Фото Pack 1 — 10 ⭐\n"
        "2. Фото Pack 2 — 20 ⭐\n"
        "3. Фото Pack 3 — 30 ⭐"
    )

# ===== ВИДЕО =====

@dp.message(F.text == "🎥 Видео")
async def videos(message: Message):
    await message.answer(
        "🎥 Видео товары:\n\n"
        "1. Video Pack 1 — 50 ⭐\n"
        "2. Video Pack 2 — 80 ⭐"
    )

# ===== RUN =====

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
