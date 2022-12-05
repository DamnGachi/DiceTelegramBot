from imports import InlineKeyboardMarkup,  Bot, Dispatcher, types, os
from loader import storage

API_TOKEN_BOT = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)

inline_button = types.InlineKeyboardButton('Bet', callback_data='Bet')
bet_money = InlineKeyboardMarkup(row_widht=1).add(inline_button)


@dp.callback_query_handler(lambda call: call.data == 'Bet')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer()

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'okay')

