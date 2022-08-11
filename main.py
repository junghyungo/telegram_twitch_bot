import telegram
from telegram.ext import Updater, MessageHandler, Filters
from twitch_api import *
from twitch_channel_list import myList

token = "5315161500:AAG3hgkmE30vw3xbElvODcFQQySGWO6FK5A"
id = 5286200749
bot = telegram.Bot(token)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

# while True:
# 	for i in myList:
# 		print(isLive(i))

def send(bot_text):
	bot.send_message(chat_id=id, text=bot_text)
	
def handler(update, context):
	user_text = update.message.text
	send(getChannel(user_text))

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)