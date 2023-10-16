# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_prices(filename):
    '''Reads the prices from a CSV file'''
    prices = []
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        for rowno, row in enumerate(reader, start=1):
            record = dict(zip(header, row))
            try:
                nsharses = int(record['shares'])
                price = float(record['price'])
                prices.append(record)
            except IndexError:
                print("Couldn't parse line", row)
    return prices

def read_portfolio(filename):
    '''Reads the portfolio from a CSV file'''
    portfolio = []
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_portfolio_dict(filename):
    '''Reads the portfolio from a CSV file'''
    portfolio = []
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def main():
    portfolio = read_portfolio_dict('Data/portfolio.csv')
    # pprint(portfolio)

    prices = read_prices('Data/prices.csv')
    # pprint(prices)
    overall_gain = 0
    for stock in portfolio:
        purchased_price = stock['price']
        amount = stock['shares']
        current_price = 0
        for price in prices:
            if price['name'] == stock['name']:
                current_price = price['price']
        gain = (current_price * amount) - (purchased_price * amount)
        overall_gain = overall_gain + gain
    print(overall_gain)

main()
