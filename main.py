from asyncio.log import logger
from crypt import methods
import os

from click import command
import telebot
import logging
from config import *
from flask import flask, request


bot = telebot.TeleBot(BOT_TOKEN)
server = flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user_username
    bot.reply_to(message, f"hello,{username}!")
    
    
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_date().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__== "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))