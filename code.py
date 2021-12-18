import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#from tapi_yandex_market import YandexMarket

#OAUTH_TOKEN = "{x}"
#OAUTH_CLIENT_ID = "{x}"

#client = YandexMarket(
#    # https://yandex.ru/dev/market/partner/doc/dg/concepts/authorization.html
#    oauth_token=OAUTH_TOKEN,
#    oauth_client_id=OAUTH_CLIENT_ID,
#    # Will retry the request if the request limit is reached.
#    retry_if_exceeded_requests_limit=True,
#)
#campaigns = client.campaigns().get()
#print(campaigns.data)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    updater = Updater("5091663511:AAH7HRxQsPBthP74USU3rAlcoVsb8npGtiI")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
