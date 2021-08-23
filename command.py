from telegram.ext import contexttypes
from currency import *

def error(update, context):
    print(f'Algo deu errado {context.error}')


def start(update, context):
    nome = update.message.chat.first_name
    update.message.reply_text(f'Welcome, {nome}! Type /help to see the currency list.')

def help(update, context):
    update.message.reply_text(
        '/start - Start bot\n'+
        '/help - Show currency list\n'+
        '\n'+
        '/realdollar - Real (BRL) to Dollar (USD)\n' +
        '/realeuro - Real (BRL) to Euro (EUR)\n' +
        '/realpound - Real (BRL) to Pound (GBP)\n' +
        '\n'+
        '/dollarreal - Dollar (USD) to Real (BRL)\n' +
        '/dollareuro - Dollar (USD) to Euro (EUR)\n' +
        '/dollarpound - Dollar (USD) to Pound (GBP)\n' +
        '\n'+
        '/euroreal - Euro (EUR) to Real (BRL)\n' +
        '/eurodollar - Euro (EUR) to Dollar (USD)\n' +
        '/europound - Euro (EUR) to Pound (GBP)\n' +
        '\n'+
        '/poundreal - Pound (GBP) to Real (GBP)\n' +
        '/pounddollar - Pound (GBP) to Dollar (USD)\n' +
        '/poundeuro - Pound (GBP) to Euro (EUR)'

    )

#BRL

def realdollar(update, context):
    real = update.message.text.replace('/realdollar','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/dolar_real

    update.message.reply_text(f'USD {convert:.2f}')


def realeuro(update, context):
    real = update.message.text.replace('/realeuro','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/euro_real

    update.message.reply_text(f'EUR {convert:.2f}')



def realpound(update, context):
    real = update.message.text.replace('/realpound','')
    real = real.replace(',','.')

    real = float(real)
    convert = real/libra_real

    update.message.reply_text(f'GBP {convert:.2f}')


#USD


def dollareuro(update, context):
    dolar = update.message.text.replace('/dollareuro','')
    dolar = dolar.replace(',','.')

    dolar = float(dolar)
    convert = dolar*dolar_euro

    update.message.reply_text(f'EUR {convert:.2f}')

def dollarpound(update, context):
    dolar = update.message.text.replace('/dollarpound','')
    dolar = dolar.replace(',','.')

    dolar = float(dolar)
    convert = dolar/libra_dolar

    update.message.reply_text(f'GBP {convert:.2f}')


def dollarreal(update, context):
    dolar = update.message.text.replace('/dollarreal','')
    dolar = dolar.replace(',','.')

    dolar = float(dolar)
    convert = dolar*dolar_real

    update.message.reply_text(f'BRL {convert:.2f}')


#EUR

def euroreal(update, context):
    euro = update.message.text.replace('/euroreal','')
    euro = euro.replace(',','.')

    euro = float(euro)
    convert = euro*euro_real

    update.message.reply_text(f'BRL {convert:.2f}')


def eurodollar(update, context):
    euro = update.message.text.replace('/eurodollar','')
    euro = euro.replace(',','.')

    euro = float(euro)
    convert = euro/dolar_euro

    update.message.reply_text(f'USD {convert:.2f}')


def europound(update, context):
    euro = update.message.text.replace('/europound','')
    euro = euro.replace(',','.')

    euro = float(euro)
    convert = euro/libra_euro

    update.message.reply_text(f'GBP {convert:.2f}')


#GBP

def poundreal(update, context):
    libra = update.message.text.replace('/poundreal','')
    libra = libra.replace(',','.')

    libra = float(libra)
    convert = libra*libra_real

    update.message.reply_text(f'BRL {convert:.2f}')


def pounddollar(update, context):
    libra = update.message.text.replace('/pounddollar','')
    libra = libra.replace(',','.')

    libra = float(libra)
    convert = libra*libra_dolar

    update.message.reply_text(f'USD {convert:.2f}')


def poundeuro(update, context):
    libra = update.message.text.replace('/poundeuro','')
    libra = libra.replace(',','.')

    libra = float(libra)
    convert = libra*libra_euro

    update.message.reply_text(f'EUR {convert:.2f}')