# chand چند؟

[![PyPI](https://img.shields.io/pypi/v/chand?style=for-the-badge)](https://pypi.org/project/chand)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chand?style=for-the-badge)](https://pypi.org/project/chand)
[![GitHub](https://img.shields.io/github/license/armanyazdi/chand?style=for-the-badge)](https://pypi.org/project/chand)

A Python library for converting currencies to Iranian Rial and Toman.

Note: This package shows the right real time price of Iranian Rial.

## Installation

Install from [PyPI](https://pypi.org/project/chand) with pip by typing in your favorite terminal.

This will also install `requests` and `bs4`.

`pip install chand`

## Usage

Let's take a look at what an example test case would look like using `chand`.

### Exchange Rates in Rial and Toman:

```python
import chand

chand.toman('usd') # or 'USD'
chand.toman('gbp') # or 'GBP'
chand.rial('eur')  # or 'EUR'
chand.rial('try')  # or 'TRY'
```

### Currency Converter:

It can convert the currency of **136 codes (ISO 4217)**.

```python
import chand

chand.convert('eur', 'usd', 500) # 500 Euro to US Dollar
chand.convert('usd', 'eur', 500) # 500 US Dollar to Euro
chand.convert('eur', 'try', 100) # 100 Euro to Turkish Lira
```

### Crypto Price in USD:

It supports more than **3700 Crypto Currencies**.

```python
import chand

chand.crypto('bitcoin')  # or 'btc'
chand.crypto('ethereum') # or 'eth'
chand.crypto('cardano')  # or 'ada'
```

### Crypto Converter:

```python
import chand

chand.convert('btc', 'eth')     # Bitcoin to Ethereum
chand.convert('eth', 'btc', 10) # 10 Ethereum to Bitcoin
chand.convert('btc', 'eur', 5)  # 5 Bitcoin to Euro
chand.convert('eth', 'gbp', 20) # 20 Bitcoin to Pound
```

### Color Formats Converter:

HEX to RGB, CMYK, HSV/HSB

```python
import chand

chand.convert('hex', 'rgb', 'ff4f5e')  # (255, 79, 94)
chand.convert('hex', 'cmyk', 'ff4f5e') # (0%, 69%, 63%, 0%)
chand.convert('hex', 'hsv', 'ff4f5e')  # (355°, 69%, 100%)
```

### BMI, BMR, RMR Calculator:

```python
import chand

chand.bmi(180, 75) # or chand.bmi('180', '75')
# Height(cm), Weight(kg)

chand.bmr(168, 55, 22, 'female')
# Height(cm), Weight(kg), Age, Sex

chand.rmr(180, 75, 29, 'male')
# Height(cm), Weight(kg), Age, Sex
```