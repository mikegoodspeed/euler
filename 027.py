class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            return self.func(*args)

@memoized
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n / 2 + 1):
        if n % i == 0:
            return False
    return True

max_n = 0
max_a_b = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime((n ** 2) + (a * n) + b):
            n += 1
        if n > max_n:
            max_n = n
            max_a_b = (a, b)
print max_n
print max_a_b
a, b = max_a_b
print a * b
