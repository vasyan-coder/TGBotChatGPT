from aiogram import Dispatcher
from aiogram.types import Message, ChatAction
from aiogram.filters import Command

from lexicon.lexicon_ru import LEXICON_RU
from services.sevices import get_chatGPT_answer


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на любое слово
async def process_other_text(message: Message):
    await message.answer(text=get_chatGPT_answer(message.text), action=ChatAction.TYPING)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands=['start', 'help']))
    dp.message.register(process_other_text)
