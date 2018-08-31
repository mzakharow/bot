import random

import telebot
from telebot.types import Message

TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types='text')
def echo_gigits(message: Message):
    if 'Hello' in message.text:
        bot.reply_to(message, 'Hi!')
    else:
        bot.reply_to(message, str(random.random()))
    return


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'Привет ' + message.chat.first_name)
    bot.send_sticker(message.chat.id, 'CAADAgADNQIAArrAlQWDyVsbzOPgPQI')
    print(message)
    # print(message.text)


bot.polling(timeout=60)
