from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb

import random
import requests
from bs4 import BeautifulSoup

url = 'http://anekdotme.ru/random'


def get_random_joke():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jokes_list = soup.find_all('div', class_='anekdot_text')
    random_joke = random.choice(jokes_list)

    return random_joke.text.strip()


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Телеграм бот с анекдотами!',
        reply_markup=kb.main)


@router.message(F.text == 'Информация')
async def info(message: Message):
    await message.answer('Бот парсит случайные анекдоты с сайта anekdotme.ru и отправляет их вам.')


@router.message(F.text == 'Анекдоты')
async def anecdotes(message: Message):
    joke = get_random_joke()
    await message.answer(f'Тебе попался данный анекдот:\n\n{joke}')