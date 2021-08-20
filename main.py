API_TOKEN = 'token' #Replace with your api token

from telegram.ext import *
from command import *

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('realdolar', realdolar))
    dp.add_handler(CommandHandler('realeuro', realeuro))
    dp.add_handler(CommandHandler('dolarreal', dolarreal))
    dp.add_handler(CommandHandler('dolareuro', dolareuro))
    dp.add_handler(CommandHandler('euroreal', euroreal))
    dp.add_handler(CommandHandler('eurodolar', eurodolar))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()