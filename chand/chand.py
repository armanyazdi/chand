import requests
from bs4 import BeautifulSoup
from re import findall
from .coins import *


def rial(currency='usd'):
    if currency == 'usd' or currency == 'USD' or currency == 'Usd':
        currency = 'dollar_rl'
        r = requests.get(f'https://www.tgju.org/profile/price_{currency.lower()}')
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(',', '')
        return price
    elif currency in coins:
        return f'{round(int(rial()) * float(crypto(currency)) * 1.0175)}'



def toman(currency='usd'):
    return rial(currency)[0:-1]


def crypto(currency='btc'):
    if len(currency) <= 6:
        currency = coins[currency.lower()].replace(' ', '-')
    else:
        currency = currency.lower().replace(' ', '-')

    r = requests.get(f'https://coinmarketcap.com/currencies/{currency}')
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', {'class': 'priceValue'}).text.replace('$', '').replace(',', '')
    return price


def convert(first, second, n=1):
    formats = ['hex', 'rgb', 'cmyk', 'hsv', 'hsb']
    if first and second.lower() in formats:
        r = requests.get(f'https://www.color-name.com/hex/{n}')
        soup = BeautifulSoup(r.text, 'html.parser')
        codes = soup.select('tr')
        data = []
        for code in codes[0:4]:
            data.append(code.find('td', {'class': 'right'}).text)
        if second == 'rgb':
            return data[1]
        elif second == 'cmyk':
            return data[2]
        elif second == 'hsv' or second == 'hsb':
            return data[3]
        else:
            return None
    elif first or second in coins:
        currency = coins[first.lower()].replace(' ', '-')
        r = requests.get(f'https://coinmarketcap.com/currencies/{currency}/{first}/{second}')
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find('div', {'class': 'priceValue'}).text
        rate = str(findall(r'[\d*\,]*\.\d*', price)).strip("[']").replace(',', '')
        return f'{int(n) * float(rate):.2f}'
    else:
        r = requests.get(f'https://www.tgju.org/profile/{first.lower()}-{second.lower()}-ask')
        soup = BeautifulSoup(r.text, 'html.parser')
        rate = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(',', '')
        return f'{int(n) * float(rate):.2f}'


def bmi(height, weight):
    bmi = float(weight) / ((float(height) / 100) ** 2)
    return f'{bmi:.2f}'


def bmr(height, weight, age, sex):
    if sex == 'male' or sex == 'm':
        bmr = 88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * int(age))
    elif sex == 'female' or sex == 'f':
        bmr = 447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * int(age))
    else:
        return None
    return round(bmr)


def rmr(height, weight, age, sex):
    if sex == 'male' or sex == 'm':
        rmr = 9.99 * int(weight) + 6.25 * int(height) - 4.92 * int(age) + 5
    elif sex == 'female' or sex == 'f':
        rmr = 9.99 * int(weight) + 6.25 * int(height) - 4.92 * int(age) - 161
    else:
        return None
    return round(rmr)
