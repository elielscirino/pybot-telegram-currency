from requests.api import get
from telegram.ext import contexttypes
import requests

site = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()
dolar = float(site['USDBRL']['high'])

def error(update, context):
    print(f'Algo deu errado {context.error}')


def start(update, context):
    nome = update.message.chat.first_name
    update.message.reply_text(f'Welcome, {nome}! Type /help to see the currency list.')

def help(update, context):
    update.message.reply_text(
        '/start - Start bot\n'+
        '/help - Show currency list\n'+
        '/realdolar - Real (BRL) to dolar (USD)\n' +
        '/dolarreal - Dolar (USD) to real (BRL)\n'
    )

def realdolar(update, context):
    real = update.message.text.replace('/realdolar','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/dolar

    update.message.reply_text(f'USD {convert:.2f}')

def dolarreal(update, context):
    real = update.message.text.replace('/dolarreal','')
    real = real.replace(',','.')

    real = float(real)
    convert = dolar*real

    update.message.reply_text(f'BRL {convert:.2f}')
    