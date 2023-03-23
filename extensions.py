import requests
import json
from config import keys

class CustomExceptions(Exception):
    pass

class CurrencyExchange:
    @staticmethod
    def convert(quote: str, base: str, amount: str):


        if quote == base:
            raise CustomExceptions(f'Нельзя переводить одну и ту же валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise CustomExceptions(f'Не смог обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise CustomExceptions(f'Не смог обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise CustomExceptions(f'Не смог обработать количество {amount}')
        if amount <= 0:
            raise CustomExceptions(f'Количество переводимой валюты должно быть больше ноля.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        course = json.loads(r.content)[keys[base]]
        return course