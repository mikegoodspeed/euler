"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their
digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import math

def num_digits(n):
    return int(math.log(n, 10))

def digits(n):
    l = []
    for i in range(num_digits(n) + 1):
        l.insert(0, n % 10)
        n = n / 10
    return l 

count = 0
for i in range(10, 1000000):
    if i == sum([x ** 5 for x in digits(i)]):
        count += i
        print count, i

