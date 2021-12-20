# Import library
from main import bot, dp
from config import admin_id
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

array_keyboard = [1, 2]

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")

# Start bot using func
async def send_to_admin (dp):
        await bot.sent_message(chat_id=778390599, text="Bot start")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keybord_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Hello!', reply_markup=keyboard_markup)
       



