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

name = '';
num = 0;

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Номер телефона?');
    bot.register_next_step_handler(message, get_num);

def get_num(message):
    global num;
    while num == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
      bot.send_message(message.from_user.id, 'Тебе '+str(num)+' лет, тебя зовут '+name+' '+'?')

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
		bot.send_message(config.owner, '`'+ str(message.from_user.id) + ': ' +'`' + message.text, parse_mode="Markdownv2")
		#bot.send_message(message.chat.id, '%s, wait please 👍'%message.chat.username)
		bot.send_message(message.chat.id, 'Йо, {0.first_name}!'.format(message.from_user, bot.get_me(), parse_mode="html"))

if __name__ == '__main__':
	bot.polling(none_stop = True)
