import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    query.message.reply_text(text=f"Selected option: {query.data}")


def echo(update: Update, context: CallbackContext) -> None:
    markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='🔎 Поиск комплектующих', callback_data='1'), InlineKeyboardButton(text='🔎 Проверка цены', callback_data='2')]])
    update.message.reply_text(update.message.text, reply_markup=markup)
    update.effective_user.id


def main() -> None:
    updater = Updater("secret")

    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
