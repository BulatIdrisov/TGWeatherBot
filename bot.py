import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from main import weather
import schedule
import time

bot = Bot("6443145925:AAFugA-zjfx8vU-JvGbjQR2Z09jmhCDK1EQ")
dispatcher = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    #await db.cmd_start_db(message.from_user.id)
    await message.answer("Привет, это бот погодник!\n"
                         "Здесь ты можешь узнать актуальную погоду в любой точке мира!\n"
                         "Напишите название населенного пункта, чтобы я показал тебе погоду")


@dispatcher.message_handler(commands=['every_day'])
async def set_daily_weather_notify(message: types.Message):
    arguments = message.get_args().split()
    if len(arguments) != 2:
        await message.answer("Please, provide city and time in the following format: /every_day city time (e.g. /every_day London 08:00)")
        return
    city, time = arguments
    print(city, time)
    schedule.every().day.at(time).do(check_weather(city))


@dispatcher.message_handler()
async def check_weather(message: types.Message):
    city = message.text
    await message.answer(weather(city))



async def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dispatcher, skip_updates=True)

