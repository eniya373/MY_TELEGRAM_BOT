!pip install adafruit.io
!pip install python-telegram-bot
# importing libraries
from Adafruit_IO import Client, Feed, Data
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os

# x=ADAFRUIT_IO_USERNAME
# y=ADAFRUIT_IO_KEY
x = os.getenv('x')
y = os.getenv('y')
Telegram_token = os.getenv('Telegram_token')
aio = Client(x,y)

feed_value=Feed(name='telegrambot')
result=aio.create_feed(feed_value)

def start(bot, update):
    bot.send_message(chat_id = update.effective_chat.id, text="WELCOME!")
    bot.send_message(chat_id = update.effective_chat.id, text="If you want to turn on the light then type in 'Turn on the light' or if you want to turn off the light then type in 'Turn off the light'")

def wrong_message(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops!,I Couldn't recognize.Please try again!!")
    
def send_data_to_adafruit(value1):
  value = Data(value=value1)
  value_send = aio.create_data('telegrambot',value)
  
def turn_on_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning on the light")
  bot.send_photo(chat_id, photo='https://cdn4.vectorstock.com/i/1000x1000/48/08/realistic-glowing-light-bulb-on-dark-background-vector-3374808.jpg')
  send_data_adafruit(1)
  
def turn_off_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning off the light")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  send_data_adafruit(0)
  
def text_given_in_tele(bot, update):
  text = update.message.text
  if text == 'Start':
    start(bot,update)
  elif text == 'Turn on the light':
    turn_on_light(bot,update)
  elif text == 'Turn off the light':
    turn_off_light(bot,update)
  else:
    wrong_message(bot,update)
    
ud = Updater('Telegram_token')
dip = ud.dispatcher
dip.add_handler(MessageHandler(Filters.text, text_given_in_tele))

ud.start_polling()
ud.idle() 
