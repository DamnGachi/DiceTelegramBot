from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor

from states.bot_registration import registration
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp


@dp.message_handler(Command('register'))
async def bot_register(message: types.Message):
    unique_name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'{message.from_user.first_name}')
            ],
            [
                KeyboardButton(text='Cancel registration')
            ]
        ],
        resize_keyboard=True
        # one_time_keyboard=True

    )
    await message.answer(f'Hi\n'
                         f'Your unique username: ',
                         reply_markup=unique_name)
    await registration.unique_name.set()


@dp.message_handler(state=registration.unique_name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    password = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Cancel')
            ],
        ],
        resize_keyboard=True
    )

    await message.answer(f'<b>{message.text}</b>, Now send me your password',
                         reply_markup=password)
    await registration.password.set()


@dp.message_handler(state=registration.password)
async def get_password(message: types, state: FSMContext):
    answer = message.text
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='cancel')
            ]
        ],
        resize_keyboard=True
    )
    try:
        if answer:
            await state.update_data(password=answer)
            await message.answer(f'Now send me your age')
            await registration.age.set()
        else:
            await message.answer('Incorrect')

    except Exception:
        await message.answer(Exception)


@dp.message_handler(state=registration.age)
async def get_age(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isnumeric():
        if int(answer) < 100:
            await state.update_data(age=answer)
            data = await state.update_data()
            unique_name = data.get('unique_name')
            password = data.get('password')
            age = data.get('age')
            await message.answer(f'Registration complete!\n'
                                 f'Name: {unique_name}\n'
                                 f'Age: {age}\n'
                                 f'Password, tap to show: {password}\n')
        else:
            await message.answer(f'Write a correct age')

    else:
        await message.answer(f'Write a correct age')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
