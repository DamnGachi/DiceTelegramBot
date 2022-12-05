from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import dp


class ValuesBet(StatesGroup):
    bet = State()


@dp.message_handler(commands=["Bet"])
async def bet(message: types.Message):
    await ValuesBet.bet.set()
    await message.reply(f"Введите вашу ставку")
