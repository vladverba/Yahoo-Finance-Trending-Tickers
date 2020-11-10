#!/usr/local/bin/python3
import requests
import bs4
from bs4 import BeautifulSoup


def parse(source):
    soup = BeautifulSoup(source.content, 'html.parser')

    ticker = []
    companyName = []
    closingPrice = []
    percentChange = []

    for tbody in soup.find_all('tbody'):
        for tr in tbody.findAll('tr'):
            for tickerCol in tr.findAll('td', class_='data-col0 Ta(start) Pstart(6px) Pend(15px)'):
                txt = tickerCol.get_text()
                # Encoding in utf-8 to remove the u character from the list
                ticker.append(txt.encode('utf-8'))
            for nameCol in tr.findAll('td', class_='data-col1 Ta(start) Pstart(10px) Miw(180px)'):
                txt = nameCol.get_text()
                companyName.append(txt.encode('utf-8'))
            for priceCol in tr.findAll('td', class_='data-col2 Ta(end) Pstart(20px)'):
                txt = priceCol.get_text()
                closingPrice.append(txt.encode('utf-8'))
            for percentCol in tr.findAll('td', class_='data-col5 Ta(end) Pstart(20px)'):
                txt = percentCol.get_text()
                percentChange.append(txt.encode('utf-8'))

    print(ticker)
    print(companyName)
    print(closingPrice)
    print(percentChange)


def main():
    session = requests.Session()
    url = 'https://finance.yahoo.com/trending-tickers'
    req = session.get(url)
    parse(req)


if __name__ == '__main__':
    main()
