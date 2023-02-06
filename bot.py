import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config

# from handlers.user_handlers import register_user_handlers

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция для регистрации всех хэндлеров
# def register_all_handlers(dp: Dispatcher) -> None:
#     register_user_handlers(dp)
#     register_other_handlers(dp)


# Функция конфигурирования и запуска бота
def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config('.env')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Регистрируем все хэндлеры
    # register_all_handlers(dp)

    # Запускаем polling
    try:
        dp.run_polling(bot)
    finally:
        # Выводим в консоль информацию о завершении работы бота
        logger.info('Bot stopped!')


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        main()
    except SystemExit:
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
