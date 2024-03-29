from aiogram import executor
from aiogram.types import BotCommand, BotCommandScopeDefault

from src.handlers import register_all_handlers
from src.filters import register_all_filters
from src.database import register_models
from src.create_bot import dp, bot
from src.middlewares.user_activity import UserActivityMiddleware
from src.utils import logger
from config import Config


async def on_startup(_):
    # Добавление команды /start
    commands = [
        BotCommand(command='start', description='Начало работы'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

    # Регистрация middlewares
    dp.middleware.setup(UserActivityMiddleware())

    # Регистрация фильтров
    register_all_filters(dp)

    # Регистрация хэндлеров
    register_all_handlers(dp)

    # Регистрация моделей базы данных
    register_models()

    logger.info('Бот запущен!')


async def on_shutdown(_):
    await (await bot.get_session()).close()


def start_bot():
    try:
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)
    except Exception as e:
        logger.error(e)

