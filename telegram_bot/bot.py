from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from django.conf import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""

    chat_id = str(update.effective_chat.id)

    await update.message.reply_text(
        f'Привет! Твой Telegram chat ID: {chat_id}\n'
        'Сохрани его для привязки к своему аккаунту.'
    )


def run_bot():
    """Запуск Telegram-бота."""

    application = Application.builder().token(
        settings.TELEGRAM_BOT_TOKEN
    ).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()