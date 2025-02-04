import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


'''бот который будет отправлять конкретную фотографию к которой будет
прекреплена инлайн клавиатура с тремя опциями'''


bot = Bot(token='7637101101:AAGFUudXYlFFtFjN5KPRCfvOs0FHpRTTK8U')
dp = Dispatcher()

is_voted = False

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Like', callback_data='like'),
         InlineKeyboardButton(text='Dislike', callback_data='dislike')],
        [InlineKeyboardButton(text='Close', callback_data='close')],
    ]
)


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    '''Команда старт и клавиатура с фотографией'''
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://i.pinimg.com/originals/83/c4/9b/83c49b48ba94efcb01d2d0bf9d5ff83b.jpg',
                         caption='Do you like?',
                         reply_markup=ikb)


@dp.callback_query(F.data == 'close')
async def ikb_close_cb_handler(callback: types.CallbackQuery):
    '''Кнопка удалить'''
    # if callback.data == 'close':
    await callback.message.delete()


@dp.callback_query()
async def ikb_close_cb_handler(callback: types.CallbackQuery):
    '''Если не голосовал голосуешь если повторно то выскакивает окошко же голосовал'''
    global is_voted
    if not is_voted:
        # await callback.answer(str(callback.data))
        if callback.data == 'like':
            await callback.answer(text='You like this photo')
            is_voted = True
        await callback.answer(text='You dislike this photo')
        is_voted = True
    await callback.answer('Your I"ve already voted', show_alert=True)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())