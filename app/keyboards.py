from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Анекдоты')],
    [KeyboardButton(text='Информация')]
], resize_keyboard=True, input_field_placeholder='Выбери пункт ниже')
