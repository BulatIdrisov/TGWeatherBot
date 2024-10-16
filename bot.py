from aiogram import Bot, Dispatcher, executor, types
from main import weather
bot = Bot("TOKEN")
dispatcher = Dispatcher(bot)
async def on_startup(_):
    print('Бот успешно запущен!')

@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, это WeatherBot!\n"
                         "Здесь ты можешь узнать актуальную погоду в любой точке мира!\n"
                         "Напиши название населенного пункта, чтобы я показал тебе погоду.")


@dispatcher.message_handler()
async def check_weather(message: types.Message):
    city = message.text
    await message.answer(weather(city))

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)

