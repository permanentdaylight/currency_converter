from currency import *


currency_codes = {
    'USD': 1,
    'EUR': .87,
    'GBP': .70
    'INR': 66,
    'AUD': 1.3,
    'CAD', 1.3
}

ict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
class CurrencyConverter:

    def __init__(self, currency_codes):
        self.currency_codes = currency_codes


        def convert(self, currency, currency_code):
            pass


cc = CurrrencyConverter({'USD':1, 'EUR': 0.74})

cc.currency_codes

cc.convert(five)

cc.convert

currency_converter.set_currenctly_codes#sending info




Must be initialized with a dictionary of currency codes to conversion rates (see link to rates below).
At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and
the other being the conversation rate. An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that
a dollar is worth 0.74 euros.
Must be able to take a Currency object and a requested currency code that is the same currency code as the
Currency object's and return a Currency object equal to the one passed in. That is,
currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').
Must be able to take a Currency object that has one currency code it knows and a requested
currency code and return a new Currency object with the right amount in the new currency code.
Must be able to be created with a dictionary of three or more currency codes and conversion rates.
An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}, which implies that a dollar is worth 0.74 euros and
that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
Must be able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
