"""
import operator

def factorial(n):
    return reduce(operator.mul, range(1, n + 1))

def sum_digits(n):
    return sum(map(int, str(n)))

print factorial(100)
print sum_digits(factorial(100))
"""
print sum(map(int, str(reduce(lambda x, y: x * y, range(1, 100 + 1)))))