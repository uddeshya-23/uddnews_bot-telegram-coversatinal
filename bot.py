import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackContext , Dispatcher
from utils import get_reply, fetch_news, topics_keyboard
##format for create logging to enable bot
logging.basicConfig(format='%(asctime)s - %(name)s - &(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1621167363:AAGIDHUYb0hQ6UCJYW7KhPA3Odo02QsNPLk"

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello!"

@app.route(f'/{TOKEN}' , methods=['GET' , 'POST'])

def webhook():
    ##webhook view which rceives updates form telegram
    
    update = Update.de_json(request.get_json(), bot)
    ##dispatcher is an object used for handling updates
    dp.process_update(update)
    return "ok"
 



def reply_text(bot, update):
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "get_news":
        articles = fetch_news(reply)

        for article in articles:
            bot.send_message(chat_id=update.message.chat_id, text=article['link'])

    else:
        bot.send_message(chat_id=update.message.chat_id, text=reply)

    
                        
##def start (bot, update: Update,context: CallbackContext):
   
  ####reply = "HI!!{}".format(author)
   ## bot.send_message(chat_id=update.message.chat_id, text=reply)

def greeting(update: Update,context: CallbackContext):
    first_name = update.to_dict()['message']['chat']['first_name']
##    print(update.to_dict().keys(),first_name)
    update.message.reply_text("hi {}".format(first_name))

def help(bot, update):
    help_txt = "Hey! i am here to help you"
    bot.send_message(chat_id=update.message.chat_id, text=help_txt)


def news(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Choose a category", reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))

##def message_handler(update: Update,context: CallbackContext):
  ##  text = update.to_dict()['message']['text']
    ##update.message.reply_text(text)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id , sticker=update.message.sticker.file_id)


def error(bot, update):
     logger.error("Update '%s' caused error '%s'", update, update.error)

     

###def main():
    ##updater = Updater(TOKEN)
  ##  bot = Bot(TOKEN)
    ##bot.set_webhook(" https://68eb21d0e63a.ngrok.io/  " +TOKEN)

   ## dp = Dispatcher(bot, None)
    ##dp = updater.dispatcher

  ##  dp.add_handler(CommandHandler("start",greeting))
  ##  dp.add_handler(CommandHandler("help",help))
  ##  dp.add_handler(MessageHandler(Filters.text, message_handler))
  ##  dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
  ##  dp.add_error_handler(error)

  ##  updater.start_polling()
  ##  logger.info("Started Polling")
  ##  updater.idle() 

bot = Bot(TOKEN)
try:
    bot.set_webhook("https://68eb21d0e63a.ngrok.io/" + TOKEN)
except Exception as e:
    print(e)

dp = Dispatcher(bot, None)
dp.add_handler(CommandHandler("start",greeting))
dp.add_handler(CommandHandler("help",help))
dp.add_handler(CommandHandler("news",news))
dp.add_handler(MessageHandler(Filters.text, reply_text ))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dp.add_error_handler(error)    
if __name__ == "__main__":
    

    app.run(port=8443)
     
    
                     
