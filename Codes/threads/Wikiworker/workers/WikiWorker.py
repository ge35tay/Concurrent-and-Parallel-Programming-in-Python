from urllib import response
import requests
from bs4 import BeautifulSoup
from lxml import html

class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    @staticmethod   # we are not use class property in this funcition, make it as a static method
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        table_rows = table.find_all('tr')

        for table_row in table_rows[1:]:
            symbol = table_row.find('td').text.strip('\n')
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)

        if response.status_code != 200:
            print("Could not get entries")
            return []
        
        yield from self._extract_company_symbols(response.text)
