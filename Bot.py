import telebot

bot = telebot.TeleBot('1048021920:AAH_kvWl8Qjr-r_OZsT5LOCKjLgp-kGMZaA')


# https://habr.com/ru/post/448310/


# @bot.message_handler(commands=['start'])
# def start_massaging(message):
#     bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'And Hello to you')


bot.polling()
