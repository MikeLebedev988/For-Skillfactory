import requests
import json
from settings import currencies


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f"Conditions is not correct. Currencies {base} are the same.")

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f"Entered currency {quote} is not correct.")

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f"Entered currency {base} is not correct.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Amount format {type(amount)} is not correct.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[currencies[base]]

        return total_base
