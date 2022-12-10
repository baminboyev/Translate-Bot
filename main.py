import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

tarjimon = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum xush kelibsiz!")



@dp.message_handler()
async def echo(message: types.Message):
    matn = message.text
    tarjima = tarjimon.translate(matn, dest='uz')
    await message.answer(tarjima.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)