import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text='👍', callback_data='like'),
         InlineKeyboardButton(text='👎', callback_data='dislike')]
    ]
)


bot = Bot(token='7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U')
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''функционал старт вывод фото и клавиатуры к ней'''
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://i.pinimg.com/originals/83/c4/9b/83c49b48ba94efcb01d2d0bf9d5ff83b.jpg',
                         caption='like or dislike',
                         reply_markup=ikb)

@dp.callback_query()
async def ikb_handler(callback: types.CallbackQuery):
    '''функция обрабатывает нажатия на калбэк кнопки ikb'''
    if callback.data == 'like':
        await callback.answer('Your like this photo')
    if callback.data == 'dislike':
        await callback.answer('Your dislike this photo')




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())