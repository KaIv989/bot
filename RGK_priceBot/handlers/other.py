from aiogram import types, Dispatcher
from creat_bot import dp, bot
from handlers import admin
import json
from datetime import datetime

<<<<<<< HEAD
=======

>>>>>>> origin/main
#### ОБЩАЯ ЧАСТЬ ###

#@dp.message_handler(content_types=["photo"])
async def get_photo(message): # Если клиент отправил фото
    await admin.authentication(message) #Отправляем проверку на аутентификацию
    name_client = admin.user_name.get(message.from_user.id, message.from_user.id)
    destination = r"C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\doc" # Путь для сохранения фото
    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download(destination) # то сохраняем его
    await bot.send_message(5182594270,
            f'Загрузка  от {name_client} {file_info.file_path} подпись {message.caption}')  # Отправляем личным сообщением мне о том что был кем то отправлено фото
    print()
    print('Подпись к', file_info.file_path, message.caption)

    #Сообщения в консоль время , сам текст, и пользователь
    print(datetime.now().strftime('%H:%M'))
    print('От', name_client)


#@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def scan_message(message: types.Message): # Если клиент отправил документ
    await admin.authentication(message)  # Отправляем проверку на аутентификацию
    name_client = admin.user_name.get(message.from_user.id, message.from_user.id)

    destination = r"C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\doc" # Путь для сохранения
    await message.document.download(destination)
    file_id = await bot.get_file(message.document.file_id)
    await bot.send_message(5182594270, f'Загрузка  от {name_client} {file_id.file_path} подпись {message.caption}')#Отправляем личным сообщением мне о том что был кем то отправлен файл

    print()
    print(f'Подпись к документу {file_id.file_path[10:]}: {message.caption}') # {Имя файла, берем из словаря}: {Подпись к файлу}

    # Сообщения в консоль время и пользователь
    print(datetime.now().strftime('%H:%M'))
    print('От', name_client)


async def echo_send(message: types.Message): # Текст
    #your_id = message.from_user.id
    #your_name = message.from_user.username

    name_client = admin.user_name.get(message.from_user.id, message.from_user.id)

    if message.text.lower()=='привет': # Здороваемся и рассказываем о себе
        await message.reply('И тебе Привет!')
        await message.answer('Я могу сказать розничную и оптовую цену, а так же посмотреть наличие на складах в Москве, Ростове и Краснодаре. \
            \nНапиши наименование интересующего тебя товара (RGK, AMO) или скопируй артикул с сайта')
    elif await admin.authentication(message): # Формируем ответ для клиента, если пройдем аутентификацию
        mt = message.text.lower().replace('rgk', '').strip().replace('-', '').replace(' ', '').replace('amo', '')
        with open(r'C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\handlers\price.json', 'r', encoding = 'utf-8') as s:
            dic = json.load(s)

        if mt in dic and isinstance(dic[mt], str) and dic[mt] in dic:
            await message.answer(dic[dic[mt]])
        elif message.text in dic:
            await message.answer(dic[message.text])
        else:
            await message.answer(f'Нет такой номенклатуры: ( {message.text} ). Я перенаправил запрос к Вашему менеджеру. Спасибо!')
            await bot.send_message(5182594270, f'От {name_client} {message.text}')

    # Сообщения в консоль время , сам текст, и пользователь
    print()
    print(datetime.now().strftime('%H:%M'), message.text)
    print('От', name_client)

    #await message.reply(message.text)  Ответное сообщение
    #await bot.send_message(message.from_user.id, message.text) #пишет в личку


def register_handlers__other(dp: Dispatcher):
    dp.register_message_handler(get_photo, content_types=["photo"])
    dp.register_message_handler(scan_message, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(echo_send)




