# -*- coding: utf-8 -*-
import string
import random
import requests
import time
import telebot
from datetime import datetime, timedelta
from telebot.types import Message
from telebot import types
from telebot import apihelper


TOKEN = '808642149:AAEjIGpL3lK2VZS8IC8ZW7WxnolKchjtTAM' #Deguste_bot

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
bot = telebot.TeleBot(TOKEN)

now = datetime.now()
fmt = now.strftime("%H:%M")


emoji = ['🍏','🍎','🍐','🍊','🍋','🍌','🍑','🍒','🍈','🍓','🍇','🍉','🥭','🍍','🥥','🥝','🍅','🍆','🌽','🌶','🥒','🥬','🥦','🥑','🥕','🥔','🍠','🥐','🥯','🍞','🥞','🍳','🥚','🧀','🥨','🥖','🥓','🥩','🍗','🍖','🦴','🌭','🥗','🥘','🥫','🍝','🍜','🍤','🥟','🍯','❤️','🧡','💛','💚','💙','💜','💞','💕','💗','💖','💘','💝','💓','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🇺🇸','🇺🇦','🇪🇪','🇫🇷','🇫🇮','🇫🇯','🇫🇴','🇩🇪','🇮🇸','🇦🇶','🇺🇳','🏴‍☠️','🏴','🇦🇮','🇮🇱','🇷🇺','😀','😃','😄','😁','😆','😅','🙂','😇','😊','☺️','🤣','😂','🙃','😉','😌','😍','🥰','😘','😝','😛','😋','😚','😙','😗','😜','🤩','🤗','😱','🥳','🤪','😙','😚','😨','🤫','🤯','🧐','😋','😛','😝','😎','🤓','👀','🤲🏻','👐🏻','🙌🏻','👏🏻','🤝','👍🏻','👊🏻','✊🏻','👈🏻','👉🏻','👇🏻','☝🏻','✋🏻','🤚🏻','🖐🏻','🖖🏻','👋🏻','🤙🏻','💪🏻','🙏🏻','💋','👄','👅','💫','⭐️','🌟','✨','⚡️','🔥','💥','🌎','☘️','🍀','🍃','🌱','🌿','🌵','🎄','🌲','🐈','🦑','🦐','🦞','🐳','🐬','🐟','🐠','🐡','🦀','❄️','☃️','☀️','💥','🌊','🍏','🍎','🍐','🍊','🍋']

temp = []
f = open('poslov_dtb2.txt', 'r')
for row in f.readlines():
	#Data = row.split()
	temp.append(row)
#print(random.choice(temp))



@bot.message_handler(commands=['start'])
def send_message(message):
	#rand = random.choice(temp)
	bot.send_message(message.chat.id, f"Я напомню, (если вспомню)")
	

	times = [11, 15, 19]
	mins = [15]

	while True:
		
		now = datetime.now()
		#print(now)
		#time.sleep(1)
		if ((now.hour in times) and (now.minute in mins)):
			#print( f"YAY !!!!!!!!!!!")
			now = datetime.now()
			bot.send_message(message.chat.id, f"{random.choice(emoji)} А не пора ли нам подкрепиться?!\nКак говорится:\n\n{random.choice(temp)}")
			time.sleep(65)
			now = datetime.now()
			#print(now)
		else:
			pass
			now = datetime.now()
		#print(f"Error")
"""

#
print(temp)






#if(now.date().hours() == 16) and (now.date().minutes() == 23):
#	bot.send_message(message.chat.id, f"Time is:\n {fmt}")


"""


bot.polling(none_stop=True)


