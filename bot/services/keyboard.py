from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подписка🔔')],
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню...')

btnBuy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='PayMaster 💳', callback_data='buySubscribe'),],

])
