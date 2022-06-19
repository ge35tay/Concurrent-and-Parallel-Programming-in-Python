from dataclasses import replace
from lxml import html
import threading
from bs4 import BeautifulSoup
import requests
import time
import random

class YahooFinancePriceSchedular(threading.Thread):
    def __init__(self, input_queue, **kwargs):    # ! read from a queue
        super(YahooFinancePriceSchedular, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    def run(self):
        while True:
            val = self._input_queue.get()  # ! queue get is a block method, which means this programm will block until a val is got
            if val == 'DONE':
                break  # !break from one thread and to another

            yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=val)
            price = yahooFinancePriceWorker.ger_price()
            print(price)
            time.sleep(random.random())   # sleep after every requests


class YahooFinancePriceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinancePriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        self.start()

    
    def ger_price(self):
        # time.sleep(30*random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        rawprice = page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')[0].text
        price = float(rawprice.replace(',', ''))   # 1000 has ,
        return price
