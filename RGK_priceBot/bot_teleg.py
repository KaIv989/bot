
from aiogram.utils import executor
from creat_bot import dp

async def on_startup(_):                   ### когда бот выйдет в онлайн, то будет соответствующее сообщение
    print('Бот вышел в онлайн')


from handlers import client, admin, other



admin.register_handlers__admin(dp)
client.register_handlers__client(dp)
other.register_handlers__other(dp)





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
