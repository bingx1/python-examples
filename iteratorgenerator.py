import random

def simple_range_generator(limit):
    offset = 0
    while offset < limit:
        yield offset
        offset +=  1

def all_even():
    n = 0
    while True:
        yield n
        n += 2

for i in simple_range_generator(10):
    print(i)
