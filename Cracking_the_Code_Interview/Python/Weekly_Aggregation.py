# Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.
'''
Example:

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]

output = [
    ['2019-01-01', '2019-01-02'], 
    ['2019-01-08'], 
    ['2019-02-01', '2019-02-02'],
    ['2019-02-05'],
]
'''

from datetime import datetime
from collections import defaultdict 

def read_date(date):
    return datetime.strptime(date, "%Y-%m-%d")

def weeks_from_date(starting_date, date):
    delta = read_date(date) - read_date(starting_date)
    return delta.days // 7

def group_by_weeks(ts):
    starting_date = ts[0]
    grouped = defaultdict(list)
    for date in ts:
        grouped[weeks_from_date(starting_date, date)].append(date)
    return list(grouped.values())

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
    '2019-02-10',
    '2019-02-11',
    '2019-02-12',
    '2019-02-15'
]
group_by_weeks(ts)