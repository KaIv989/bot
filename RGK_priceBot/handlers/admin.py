from aiogram import types, Dispatcher
from creat_bot import bot
from r import loading


user_name = {5182594270: 'Кадацкий Иван',
             1755935932: 'Ромазин Александр',
             373640938: 'Волобуев Антон',
             638270163: 'Пальмира Анна',
             963844711: 'Альманах Дмитрий'}


async def authentication(message): # аутентификация
    if not user_name.get(message.from_user.id):
        print(user_name.get(message.from_user.id))
        await message.answer('Вы не зарегистрированы, напишите своему менеджеру.')
        await bot.send_message(5182594270, f'нужно зарегистрировать {message.from_user.id}')
        return False
    return True


async def admin_output(message: types.Message): # Написать клиенту
    if message.from_user.id == 5182594270:
        data = message.text.split()
        await bot.send_message(int(data[1]), f"Важно!!!\n{' '.join(data[2:])}")

async def admin_download(message: types.Message): # Загружаем файлы, делаем json
    if message.from_user.id == 5182594270:
        print('Загружаем файлы')
        loading(r"C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\pr.xlsx",
                r"C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\KIP.xlsx",
                r"C:\Users\User\Desktop\MF620CMFDriverV2160W64RU\bot\RGK_priceBot\Sklad.xlsx")
        await bot.send_message(5182594270, 'Остатки загружены')

def register_handlers__admin(dp: Dispatcher):
    dp.register_message_handler(admin_output, commands=['письмо'])
    dp.register_message_handler(admin_download, commands=['загрузить'])
