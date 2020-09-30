from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client,Data
import os

ADAFRUIT_IO_USERNAME =  os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_value(value):
  feed = aio.feeds('telegram_app_bot')
  aio.send_data(feed.key,value)
    
def start(update,context):
  start_message='''
/turnoff the light or 'turn off':To turn off the bulb ,sends value=0 in feed
/turnon the light or 'turn on'  :To turn on the bulb ,sends value=1 in feed
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
    
def turnonthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Turning on the bulb")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://cdn4.vectorstock.com/i/1000x1000/48/08/realistic-glowing-light-bulb-on-dark-background-vector-3374808.jpg')
  send_value(1)
def turnoffthelight(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Turning off the bulb")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  send_value(0)

def message_given(update, context):
  text=update.message.text
  if text == 'Start':
    start(update,context)
  if text == 'Turn on the light':
    turnonthelight(update, context)
    send_value(1)
  elif text == 'Turn off the light':
    turnoffthelight(update, context)
    send_value(0)
    
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
updater=Updater(TELEGRAM_TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoffthelight',turnoffthelight))
dispatcher.add_handler(CommandHandler('turnonthelight',turnonthelight))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
