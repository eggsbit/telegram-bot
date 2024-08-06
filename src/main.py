import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Let's click on the 'Play game' button to start playing!",
    )


def main() -> None:
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
