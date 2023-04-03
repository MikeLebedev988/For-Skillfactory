import requests
import json
from settings import currencies


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f"Conditions is not correct. Currencies {base} are the same.")

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConversionException(f"Entered currency {quote} is not correct.")

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConversionException(f"Entered currency {base} is not correct.")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Amount format {type(amount)} is not correct.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[currencies[base]]

        return total_base
