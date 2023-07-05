from datetime import datetime
from aiogram.utils import executor

from create_bot import dp
from handlers.questions import f


f()


async def on_startup(_):
    print('Start bot:', datetime.now())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
