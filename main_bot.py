import telebot
import properties.config
from models.models import User

props = properties.config
bot = telebot.TeleBot(props.bot_key)


# https://habr.com/ru/post/448310/


# @bot.message_handler(commands=['start'])
# def start_massaging(message):
#     bot.send_message(message.chat.id, 'Hello')

artist = User.get(User.id == 34343)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'And Hello to you')


bot.polling()
