from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подписка🔔')],
    [KeyboardButton(text='О НАС🔎')],
    [KeyboardButton(text='Договор оферты📌')],
    [KeyboardButton(text='СМЫСЛ МЕНТАЛИТЕТА ПОБЕДИТЕЛЯ📢')],
    [KeyboardButton(text='Стоимость, условия,возврат и суть работы')],
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню...')

btnBuy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='PayMaster 💳', callback_data='buySubscribe'),],

])
