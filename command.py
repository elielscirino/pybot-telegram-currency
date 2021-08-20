from requests.api import get
from telegram.ext import contexttypes
import requests

site = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,USD-EUR').json()
dolar_real = float(site['USDBRL']['high'])
euro_real = float(site['EURBRL']['high'])
dolar_euro = float(site['USDEUR']['high'])


def error(update, context):
    print(f'Algo deu errado {context.error}')


def start(update, context):
    nome = update.message.chat.first_name
    update.message.reply_text(f'Welcome, {nome}! Type /help to see the currency list.')

def help(update, context):
    update.message.reply_text(
        '/start - Start bot\n'+
        '/help - Show currency list\n'+
        'REAL (BRL)\n' +
        '/realdolar - Real (BRL) to Dolar (USD)\n' +
        '/realeuro - Real (BRL) to Euro (EUR)\n' +
        'DOLAR (USD)\n' +
        '/dolarreal - Dolar (USD) to Real (BRL)\n' +
        '/dolareuro - Dolar (USD) to Euro (EUR)\n' +
        'EURO (EUR)\n' +
        '/euroreal - Euro (EUR) to Real (BRL)\n' +
        '/eurodolar - Euro (EUR) to Dolar (USD)\n'
    )

def realdolar(update, context):
    real = update.message.text.replace('/realdolar','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/dolar_real

    update.message.reply_text(f'USD {convert:.2f}')

def dolarreal(update, context):
    real = update.message.text.replace('/dolarreal','')
    real = real.replace(',','.')

    real = float(real)
    convert = dolar_real*real

    update.message.reply_text(f'BRL {convert:.2f}')

def realeuro(update, context):
    real = update.message.text.replace('/realeuro','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/euro_real

    update.message.reply_text(f'EUR {convert:.2f}')

def euroreal(update, context):
    real = update.message.text.replace('/euroreal','')
    real = real.replace(',','.')

    real = float(real)
    convert = real*euro_real

    update.message.reply_text(f'BRL {convert:.2f}')

def dolareuro(update, context):
    dolar = update.message.text.replace('/dolareuro','')
    dolar = dolar.replace(',','.')

    dolar = float(dolar)
    convert = dolar*dolar_euro

    update.message.reply_text(f'EUR {convert:.2f}')

def eurodolar(update, context):
    dolar = update.message.text.replace('/eurodolar','')
    dolar = dolar.replace(',','.')

    dolar = float(dolar)
    convert = dolar/dolar_euro

    update.message.reply_text(f'USD {convert:.2f}')