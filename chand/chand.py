import requests
from bs4 import BeautifulSoup


def rial(currency):
    if currency == 'usd' or currency == 'USD' or currency == 'Usd':
        currency = 'dollar_rl'

    response = requests.get(f'https://www.tgju.org/profile/price_{currency.lower()}')
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find("span", {"data-col": "info.last_trade.PDrCotVal"}).text.replace(',', '')
    return price


def toman(currency):
    return rial(currency)[0:-1]


def convert(first, second, n):
    response = requests.get(f'https://www.tgju.org/profile/{first.lower()}-{second.lower()}-ask')
    soup = BeautifulSoup(response.text, 'html.parser')
    rate = soup.find("span", {"data-col": "info.last_trade.PDrCotVal"}).text.replace(',', '')
    return f'{int(n) * float(rate):.2f}'
