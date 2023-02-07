# TGBotChatGPT

[![BOT - LINK](https://img.shields.io/static/v1?label=BOT&message=LINK&color=229ed9&style=for-the-badge)](https://t.me/verystupidshitBot)
[![python](https://img.shields.io/badge/-Python-346998?style=for-the-badge&labelColor=black&logo=python&logoColor=346998)](#) 
[![aiogram](https://img.shields.io/badge/-Aiogram-009cfb?style=for-the-badge&labelColor=009cfb&logo=aiogram&logoColor=009cfb)](#) 

## Languages
<code>[Ru](README._ru.md)</code>

<code>[En](README.md)</code>

## About Project

The telegram bot project provides an opportunity to use ChatGPT-3 for free.

The project is written in Python and using the aiogram3 library.

The project is under active development, so there may be errors or pieces of shit code.

## Run the bot manually

1. Install all required dependencies using the requirements.txt file:

```
pip install -r requirements.txt
```

2. Add a file `.env` to the root directory of the project and fill it like `.env.example`
3. Run the bot:

```
python3 bot.py
```

## Running a bot with Docker

1. Create a container image:

```
docker build -t tg_bot_chatgpt
```

2. Run the container image with the command:

```
docker run --restart on-failure -e BOT_TOKEN=<TELEGRAM_TOKEN> OPENAI_TOKEN=<OPENAI_TOKEN> -t tg_bot_chatgpt
```