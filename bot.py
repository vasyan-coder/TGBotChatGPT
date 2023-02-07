import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config

from handlers.user_handlers import register_user_handlers

from external_services.openai_init import openai_init

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)


# Функция конфигурирования и запуска бота
async def main() -> None:
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
    register_all_handlers(dp)

    # Инициализируем openai сервис
    openai_init()

    # Запускаем polling
    try:
        await dp.start_polling(bot)
    finally:
        # Выводим в консоль информацию о завершении работы бота
        await bot.session.close()
        logger.info('Bot stopped!')


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except SystemExit:
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
