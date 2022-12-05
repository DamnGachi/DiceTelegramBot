from aiogram.dispatcher.filters.state import StatesGroup, State


class registration(StatesGroup):
    unique_name = State()
    password = State()
    age = State()
