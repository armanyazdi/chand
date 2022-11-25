# chand

[![PyPI](https://img.shields.io/pypi/v/chand?style=for-the-badge)](https://pypi.org/project/chand)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chand?style=for-the-badge)](https://pypi.org/project/chand)
[![GitHub](https://img.shields.io/github/license/armanyazdi/chand?style=for-the-badge)](https://pypi.org/project/chand)

A Python library for converting currencies to Iranian Rial and Toman.

# Installation

Install from [PyPI](https://pypi.org/project/chand) with pip by typing in your favorite terminal 
(This will also install `requests` and `bs4`):

`pip install chand`

# Usage

Let's take a look at what an example test case would look like using `chand`.

#### Exchange rates in Iranian Rial and Toman:

```python
import chand

chand.toman('usd') # or chand.toman('USD')
chand.rial('usd')  # or chand.rial('USD')
```
Example:
```python
import chand

USDIRR = chand.rial('usd')
EURIRR = chand.rial('eur')
EURIRT = chand.toman('eur')

print('1 USD equals:', USDIRR, 'Rials.')  # 1 USD equals: 349900 Rials
print('1 EUR equals:', EURIRR, 'Rials.')  # 1 EUR equals: 368110 Rials
print('1 EUR equals:', EURIRT, 'Tomans.') # 1 EUR equals: 36811 Tomans
```

#### Currency convertor:

It can convert the currency of **136 codes (ISO 4217)**.

```python
import chand

chand.convert('eur', 'usd', 5000) # 5000 EUR to USD
chand.convert('usd', 'try', 1000) # 1000 USD to TRY
```
Example:
```python
import chand

USDEUR = chand.convert('usd', 'eur', 1000)
EURUSD = chand.convert('eur', 'usd', 1000)
USDTRY = chand.convert('usd', 'try', 100)

print('1000 USD equals:', USDEUR, 'EUR.') # 1000 USD equals: 960.20 EUR
print('1000 EUR equals:', EURUSD, 'USD.') # 1000 EUR equals: 1040.90 USD
print('100 USD equals:', USDTRY, 'TRY.')  # 100 USD equals: 1863.82 TRY
```