from aiogram import Bot, Dispatcher, executor, types
import asyncio


@dp.message_handler(commands=["Dice"])
async def dice(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Бот кидает кубик")
    await asyncio.sleep(1)
    bot_data = await bot.send_dice(chat_id)
    bot_data = bot_data['dice']['value']
    await asyncio.sleep(4)
    await bot.send_message(chat_id, "Вы кидаете кубик")
    await asyncio.sleep(1)
    user_data = await bot.send_dice(chat_id)
    user_data = user_data['dice']['value']
    if bot_data > user_data:
        await asyncio.sleep(4)
        await bot.send_message(chat_id, f"Your number ['value'], You lose")
    elif bot_data < user_data:
        await asyncio.sleep(4)
        await bot.send_message(chat_id, f"Your number ['value'], You win!")
    elif bot_data == user_data:
        await asyncio.sleep(4)
        await bot.send_message(chat_id, f"Draw!")
