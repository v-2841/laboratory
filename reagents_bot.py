import locale
import os
import psycopg2

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


load_dotenv()
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
updater = Updater(token=os.getenv('TELEGRAM_TOKEN', 'token'))


def data_handler(data):
    if not data:
        return 'Ничего не найдено!'
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


def search_by_name(name):
    connection = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'laboratory'),
        user=os.getenv('POSTGRES_USER', 'django_user'),
        password=os.getenv('POSTGRES_PASSWORD', ''),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', 5432)
    )
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM reagents_reagent WHERE name ILIKE %s"
        cursor.execute(query, ('%' + name + '%',))
        results = cursor.fetchall()
        return data_handler(results)
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        connection.close()


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=(
        'Привет, я лабораторный помощник! Введите частичное название '
        + 'реактива и я выдам вам информацию о его наличии.')
    )


def search(update, context):
    chat = update.effective_chat
    name = update.message.text
    context.bot.send_message(chat_id=chat.id,
                             text=search_by_name(name))


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, search))
updater.start_polling()
updater.idle()
