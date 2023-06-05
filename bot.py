import logging
import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}")

@dp.message(Command("hi")) 
async def start(message: types.Message):
    await message.reply("Hi!")

@dp.message(Command("dice"))
async def dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

@dp.message(Command("football"))
async def football(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)
    
@dp.message()
async def text(message: types.Message):
    await message.answer(message.text)    

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())