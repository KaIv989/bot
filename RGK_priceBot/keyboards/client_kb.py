from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1=KeyboardButton('/Расположение\Режим_работы_Ростов-на-Дону')
b2=KeyboardButton('/Расположение\Режим_работы_Краснодар')

kb_client= ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2)



