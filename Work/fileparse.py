# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=','):
    '''
    Parses a CSV file into a list of records
    '''
    with open(filename, 'rt') as f:
        reader = csv.reader(f, delimiter=delimiter)
        headers = []
        indices = []
        if has_headers:
            headers = next(reader)
            if select:
                indices = [headers.index(name) for name in select]
                headers = select

        records = []
        for row in reader:
            if not row:
                continue
            if indices:
                row = [ row[index] for index in indices ]
            if types:
                row = [ func(val) for func, val in zip(types, row) ]

            record = dict(zip(headers, row))
            records.append(record)
    return records
