'''
This is portfolio program
This is multiline comment
\ - start from same line. if its not put, it goes to new line

Acquire stock information and convert into convenient form'

_ - underscore is to refer last object ..print(_)
'''
import csv

from collections  import namedtuple

Trade = namedtuple('Trade',['symbol', 'shares', 'price'])


'''with open('notes/stocks.txt') as f:
    csvfile = csv.reader(f)
    for row in csvfile:
        print(row)
'''
def get_portfolio(filename):
    stocks = []
    f = open(filename)
    for line in f:
        stock = line.rstrip().split(',')
        symbol, shares, price = stock
        stock = Trade(symbol, int(shares), float(price))
        stocks.append(stock)
    return stocks


if __name__ == '__main__':
    filename = 'notes/stocks.txt'
    port = get_portfolio(filename)
    print(port)
