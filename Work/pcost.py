# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                total = total + (int(row[1]) * float(row[2]))
            except ValueError:
                print("Couldn't parse line", line)
    return total


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost', cost)

main()
