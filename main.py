import asyncio

from aiogram import Bot, Dispatcher, executor  # Бот, доставщик объектов, запуск бота
from config import BOT_TOKEN

# Поток, в котором обрабатываются все события
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")  # мод для форматирования
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    # запуск бота, poling делает встроение запросы get update, запоминает offset, доставляет нам сообщения
    executor.start_polling(dp, on_startup=send_to_admin) #на запуске бота запускаем функцию


# для Markdown
"__italic__"  # подчёркнутое сообщение
"**bold**"  # жирное подчёркивание

# для HTML
# <i>italic</i>
# <b>bold</b>

