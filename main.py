import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from async_feedparse import async_nyaa_parse
from dmhy_feedparser import async_dmhy_parse
import tempfile

TOKEN = os.environ['telegram_bot_key']

logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Sends explanation on how to use the bot."""
  await update.message.reply_text(
    "This is a feedparser bot,only dmhy and nyaa available.\nCommand list:\n/parsenyaa\n/parsedmhy"
  )


async def parsenyaa(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = update.message.text
  command, url = message.split(" ")
  links = await async_nyaa_parse(url)
  user_get = "\n".join(links)
  await update.message.reply_text(user_get)


async def parsedmhy(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = update.message.text
  command, url = message.split(" ")
  links = await async_dmhy_parse(url)
  user_get = "\n".join(links)

  with tempfile.NamedTemporaryFile(mode="w+") as templink_text:
    # await update.message.reply_text(user_get)
    # with open("links.txt", "w") as link_text:
    templink_text.write(user_get + "\n")
    templink_text.seek(0)
    await update.message.reply_document(document=templink_text,
                                        filename='links.txt')


def main() -> None:
  """Run bot."""
  # Create the Application and pass it your bot's token.
  application = Application.builder().token(TOKEN).build()

  # on different commands - answer in Telegram
  application.add_handler(CommandHandler(["start", "help"], start))
  application.add_handler(CommandHandler(["parsenyaa"], parsenyaa))
  application.add_handler(CommandHandler(["parsedmhy"], parsedmhy))
  # Run the bot until the user presses Ctrl-C
  application.run_polling()


if __name__ == "__main__":
  main()
