import requests
from ..utils import normalize_ticker_poloniex

class API(object):
    BASE_URL = 'https://poloniex.com'
    def __init__(self, credentials=None):
        self.credentials = credentials

    def ticker(self):
        url = "{}/public".format(self.BASE_URL)
        qstring = {
            'command': 'returnTicker'
        }
        response = requests.get(url, params=qstring).json()
        response = normalize_ticker_poloniex(response)
        return response