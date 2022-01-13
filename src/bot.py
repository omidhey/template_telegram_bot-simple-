import os

import emoji
import telebot
from loguru import logger

from src.constants import keyboards
from src.utils.io import write_json

class Bot:
    """
    Template for Telegram bot.
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
        logger.info('Bot is running...!')
        self.bot.infinity_polling()

    def echo_all(self, message):
        #self.bot.reply_to(message, message.text)
        write_json(message.json, 'message.json')
        self.bot.send_message(message.chat.id, message.text, reply_markup=keyboards.main)
        print(emoji.demojize(message.text))
if __name__ == '__main__':
    logger.info('Bot Started')
    bot = Bot()
    bot.run()
    logger.info('Done!')
