'''Show how powerful list comprehensions are for testing and data analysis


    Syntax for a set comprehension:
        { <expr> for <var> in <interable> if <cond> }

    Syntax for a list comprehension:
        [ <expr> for <var> in <interable> if <cond> ]

'''

import portfolio
from pprint import pprint

port = portfolio.get_portfolio('notes/stocks.txt')

print('Projections ==Looking at a subset of the columns')
print([trade.symbol for trade in port])
print([trade.shares for trade in port])
print([trade.price for trade in port])
print()

print('How many shares of Cisco have you purchase cumulatively?')
print('SELECT SUM(shares) FROM Port WHERE symbol = "CSCO";')
print(sum([trade.shares for trade in port if trade.symbol == 'CSCO']))

print('Make an alphabetical list of the companies you have traded')
print('SELECT DISCTINCT symbol FROM Port ORDER BY symbol;')
print(sorted({trade.symbol for trade in port}))

print('how much have you invested cumulatively')
print('SELECT SUM(shares*price) FROM port')
print(sum(trade.shares * trade.price for trade in port))
