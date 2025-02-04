import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.formatting import Text

'''машина состояний - '''



storage = MemoryStorage() # хранилище

bot = Bot(token='7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U')
dp = Dispatcher(storage=storage)


def get_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='start work')]
        ]
    )
    return kb

def get_cancel():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='cancel')]
        ]
    )
    return kb


class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('welcome',
                         reply_markup=get_keyboard())


@dp.message(lambda message: not message.photo, ClientStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('This is not photo')


@dp.message(lambda message: message.photo,ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.get_data() as data:
        data['photo'] = message.photo[0].file_id
    await ClientStatesGroup.next()
    await message.reply('description')


@dp.message(Command('cancel'))
async def cmd_start(state: FSMContext):
    curr_state = state.get_state()
    if curr_state is None:
        return
    await state.clear()


@dp.message(F.text.endswith('work'))
async def start_work(message: types.Message, state: FSMContext):
    await state.set_state(ClientStatesGroup.photo)
    await message.answer('Input photo',
                         reply_markup=get_cancel())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())