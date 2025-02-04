import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


'''Счетчик использую инлайн и калбэк данные  а так же отображение рандомного числа'''


bot = Bot(token='7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U')
dp = Dispatcher()
cb = CallbackData(foo='ikb', bar='action')

ikb =InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Button', callback_data='hello')]
    ]
)


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''команда старт и отображение клавиатуры с текстом'''
    await message.answer('Text', reply_markup=ikb)





@dp.callback_query()
async def ikb_cb_handler(callback: types.CallbackQuery):
    await callback.answer('Sometime')







async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())