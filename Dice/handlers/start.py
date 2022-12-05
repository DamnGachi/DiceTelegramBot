from aiogram import Bot, Dispatcher, executor, types
from loader import dp, bot


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.reply("Hi!\nI'm DiceBot!")
    chat_id = message.chat.id
    await bot.send_message(chat_id, "click to place a bet ")