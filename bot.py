# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Добрый день! Я - {1.first_name}, оператор службы доставки.  Что привело вас сегодня к нам?'.format(message.from_user, bot.get_me(), parse_mode="html"))

    

#@bot.message_handler(commands=["help"])
#def start(message):
	#bot.send_message(message.chat.id, 'Help')

#message.from_user.id
#message.from_user.first_name
#message.from_user.last_name
#message.from_user.username

@bot.message_handler(content_types=["text"])
def messages(message):

	if int(message.chat.id) == int(config.owner):
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		bot.send_message(config.owner, '@' + message.from_user.username + ' ' + '`' + str(message.from_user.id) + '`' + ': ' + message.text)
		#bot.send_message(message.chat.id, '%s, wait please 👍'%message.chat.username)
		bot.send_message(message.chat.id, 'Йо, {0.first_name}!'.format(message.from_user, bot.get_me(), parse_mode="html"))

if __name__ == '__main__':
	bot.polling(none_stop = True)
