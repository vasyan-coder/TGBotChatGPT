# TGBotChatGPT

[![BOT - LINK](https://img.shields.io/static/v1?label=BOT&message=LINK&color=229ed9&style=for-the-badge)](https://t.me/verystupidshitBot)
[![python](https://img.shields.io/badge/-Python-346998?style=for-the-badge&labelColor=black&logo=python&logoColor=346998)](#) 
[![aiogram](https://img.shields.io/badge/-Aiogram-009cfb?style=for-the-badge&labelColor=009cfb&logo=aiogram&logoColor=009cfb)](#) 

## Языки

<code>[Ru](README._ru.md)</code>

<code>[En](README.md)</code>

## О проекте

Проект - телеграм бот бесплатно предоставляет возможность использовать ChatGPT-3.

Проект написан на языке Python и использованием библиотеки aiogram3.

Проект находится в стадии активной разработки, поэтому возможны ошибки или куски говнокода.

## Запуск бота вручную

1. Установите все необходимые зависимости, используя файл requirements.txt:

```
pip install -r requirements.txt
```

2. Добавьте файл `.env` в корневую директорию проекта и заполните его по примеру `.env.example`
3. Запустите бота:

```
python3 bot.py
```

## Запуск бота с помощью Docker

1. Создайте образ контейнера:

```
docker build -t tg_bot_chatgpt
```

2. Запустите образ контейнера с помощью команды:

```
docker run --restart on-failure -e BOT_TOKEN=<TELEGRAM_TOKEN> OPENAI_TOKEN=<OPENAI_TOKEN> -t tg_bot_chatgpt
```