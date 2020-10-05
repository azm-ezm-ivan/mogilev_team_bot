import telebot
from PIL import Image

from images.loggers.bot_logger import init_logger
from models.models import *
from properties import config

LOG = init_logger(config.logging_level)
bot = telebot.TeleBot(config.bot_key)
# https://habr.com/ru/post/448310/


@bot.message_handler(commands=['start'])
def start_massaging(message):
    photo = Image.open('images/maks.png')
    bot.send_photo(message.chat.id, photo, caption='Хеллёу май диа френд. Менья зовут Максим. Рад тому что меня сюда впиндюрили')
    bot.send_message(message.chat.id, 'What\'s uuuuppp man!')


#artist = User.get(User.id == 34343)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'And Hello to you')


bot.polling()
