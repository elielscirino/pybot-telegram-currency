API_TOKEN = 'token' #Replace with your api token

from telegram.ext import *
from command import *

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    #BRL
    dp.add_handler(CommandHandler('realdollar', realdollar))
    dp.add_handler(CommandHandler('realeuro', realeuro))
    dp.add_handler(CommandHandler('realpound', realpound))

    #USD
    dp.add_handler(CommandHandler('dollarreal', dollarreal))
    dp.add_handler(CommandHandler('dollareuro', dollareuro))
    dp.add_handler(CommandHandler('dollarpound', dollarpound))

    #EUR
    dp.add_handler(CommandHandler('euroreal', euroreal))
    dp.add_handler(CommandHandler('eurodollar', eurodollar))
    dp.add_handler(CommandHandler('europound', europound))
    
    #GBP
    dp.add_handler(CommandHandler('poundreal', poundreal))
    dp.add_handler(CommandHandler('pounddollar', pounddollar))
    dp.add_handler(CommandHandler('poundeuro', poundeuro))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

