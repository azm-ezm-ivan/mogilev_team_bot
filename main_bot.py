import telebot
from PIL import Image
from telebot import types

from images.loggers.bot_logger import init_logger
from models.models import *
from properties import config

LOG = init_logger()
bot = telebot.TeleBot(config.bot_key)
# https://habr.com/ru/post/448310/

user = bot.get_me()


@bot.message_handler(commands=['start'])
def start_massaging(message):
    photo = Image.open('images/maks.png')
    bot.send_photo(message.chat.id, photo,
                   caption='Хеллёу май диа френд. Менья зовут Максим. Рад тому что меня сюда впиндюрили')
    bot.send_message(message.chat.id, 'What\'s uuuuppp man!')


# artist = User.get(User.id == 34343)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hello':
        markup = types.ReplyKeyboardMarkup(selective=False)
        markup.row('a', 'v', 'd')
        bot.send_message(message.chat.id, message, reply_markup=markup)


bot.polling()
