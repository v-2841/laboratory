import locale
import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

import asyncpg
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters


load_dotenv()
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
Path('bot_logs/').mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(name)s, %(levelname)s, %(funcName)s, %(message)s',
    handlers=[RotatingFileHandler(
        'bot_logs/main.log', maxBytes=100000, backupCount=10)],
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def data_handler(data):
    result = ''
    for reagent in data:
        result += (
            f'Индекс: {reagent[1] if reagent[1] else "н/у"}\n'
            + f'Название: {reagent[2]}\n'
            + f'Марка: {reagent[3] if reagent[3] else "н/у"}\n'
            + f'Количество, г: {reagent[4] if reagent[4] else "н/у"}\n'
            + 'Дата производства: '
            + f'{reagent[5].strftime("%d %B %Y") if reagent[5] else "н/у"}\n'
            + 'Годен до: '
            + f'{reagent[6].strftime("%d %B %Y") if reagent[6] else "н/у"}\n\n'
        )
    if len(result) > 4000:
        result = result[:4000]
        result += ('\n\nСлишком много вариантов! Уточните название.')
    return result


async def search_by_name(name):
    try:
        results = await application.bot_data['database'].fetch(
            f"SELECT * FROM reagents_reagent WHERE name ILIKE '%{name}%'")
        if not results:
            return 'Ничего не найдено!'
        return await data_handler(results)
    except Exception as error:
        logger.error(error)
        return 'Ошибка приложения'


async def wake_up(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text=(
        'Привет, я лабораторный помощник! Введите частичное название '
        + 'реактива и я выдам вам информацию о его наличии.')
    )
    logger.info(f'Пользователь {chat.id} включил бота')


async def search(update, context):
    chat = update.effective_chat
    name = update.message.text
    await context.bot.send_message(chat_id=chat.id,
                                   text=await search_by_name(name))
    logger.info(f'Пользователь {chat.id} ищет реактив "{name}"')


async def post_init(application: Application) -> None:
    application.bot_data['database'] = await asyncpg.connect(
        database=os.getenv('POSTGRES_DB', 'laboratory'),
        user=os.getenv('POSTGRES_USER', 'django_user'),
        password=os.getenv('POSTGRES_PASSWORD', ''),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', 5432),
    )


async def post_shutdown(application: Application) -> None:
    await application.bot_data['database'].close()


if __name__ == '__main__':
    application = Application.builder().token(
        os.getenv('TELEGRAM_TOKEN', 'token')).post_init(
            post_init).post_shutdown(post_shutdown).build()
    application.add_handler(CommandHandler('start', wake_up))
    application.add_handler(MessageHandler(filters.TEXT, search))
    application.run_polling()
