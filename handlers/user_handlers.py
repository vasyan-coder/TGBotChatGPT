from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from lexicon.lexicon_ru import LEXICON_RU
# from services.services import get_bot_choice, get_winner


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands=['start', 'help']))
