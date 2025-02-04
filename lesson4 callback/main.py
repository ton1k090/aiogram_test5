import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


'''Счетчик использую инлайн и калбэк данные'''


bot = Bot(token='7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U')
dp = Dispatcher()

number = 0 # Глобальный счетчик для изменения в будущем

def get_inline_keyboard():
    '''Создание инлайн клавиатуры в рамках функции'''
    ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Increase', callback_data='btn_increase'),
             InlineKeyboardButton(text='Decrease', callback_data='btn_decrease')]
        ]
    )
    return ikb


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''команда старт и отображение клавиатуры с текстом'''
    await message.answer(f'Current number is {number}',
                         reply_markup=get_inline_keyboard())


@dp.callback_query(F.data.startswith('btn'))
async def ikb_cb_handler(callback: types.CallbackQuery):
    '''Обработка калбэк кнопок увеличение и уменьшение счетчика'''
    global number  # обращаемся к глобальной переменной
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'Current number is {number}',
                                         reply_markup=get_inline_keyboard())
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'Current number is {number}',
                                         reply_markup=get_inline_keyboard())
    else:
        1/0









async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())