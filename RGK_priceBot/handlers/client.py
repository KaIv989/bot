from aiogram import types, Dispatcher
from creat_bot import dp, bot
from keyboards import kb_client

#@dp.message_handler(commands=['start', 'help'])  Декоратор нужен если пишем все в одном файле.
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Слушаю', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напишите боту: \nhttps://t.me/RGK_priceBot') # если человек не разу не общался с ботом, то в ответ предложим ему пройти по ссылке


async def rgk_place_krd_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г. Краснодар, ул. Стасова д. 183,\
        Работаем: Пн-Пт с 9:00 до 18:00, в праздничные дни - не работаем')

#@dp.message_handler(commands=['Расположение'])  Декоратор нужен если пишем все в одном файле.
async def RGK_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г.Ростов-на-Дону, ул. Привокзальная 9А,\
        Работаем: Пн-Пт с 9:00 до 18:00, в праздничные дни - не работаем')


def register_handlers__client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])            
    dp.register_message_handler(rgk_place_krd_command, commands=['Расположение\Режим_работы_Краснодар'])
    dp.register_message_handler(RGK_place_command, commands=['Расположение\Режим_работы_Ростов-на-Дону'])
