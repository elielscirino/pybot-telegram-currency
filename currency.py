import requests

moeda = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,GBP-USD,GBP-EUR,USD-EUR').json()

#Cash comparing to other cash

dolar_real = moeda['USDBRL']['high']
dolar_euro = moeda['USDEUR']['high']

euro_real = moeda['EURBRL']['high']

libra_real = moeda['GBPBRL']['high']
libra_euro = moeda['GBPEUR']['high']
libra_dolar = moeda['GBPUSD']['high']