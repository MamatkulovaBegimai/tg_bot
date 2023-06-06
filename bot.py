import logging
import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton

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
    
@dp.message(Command("special_button"))
async def special_button(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Отпарвка номера", request_contact = True),
        types.KeyboardButton(text="Отпарвка геолокации", request_location=True),
    )
    builder.row(types.KeyboardButton(
        text="Создать викторину", 
        request_poll = types.KeyboardButtonPollType(type="quiz")
    ))
       
    await message.answer(
        "Выберите действие: ",
        reply_markup=builder.as_markup(resize_keyboard = True)
    )

@dp.message(Command("inline_button"))
async def inline_button(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com/"
    ))
    builder.row(types.InlineKeyboardButton(
        text="Telegram",
        url="tg://resolve?domain=telegram"
    ))
    
    user_id = 1312702673
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text="Какой-то пользователь",
            url=f"tg://user?id={user_id}"
        ))
    
    await message.answer(
        "Выберите ссылку",
        reply_markup=builder.as_markup(),
    )
    
# @dp.message()
# async def text(message: types.Message):
#     await message.answer(message.text)  
    
@dp.message(Command('id'))
async def id(message: types.Message):   
    await message.answer(message.from_user.id)       

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
    
    
