# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

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
    pprint(portfolio)

main()
