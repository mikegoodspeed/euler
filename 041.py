def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int((n ** .5) + 1)):
        if n % i == 0:
            return False
    return True

def digits(n):
    result = []
    while n:
        result.append(n % 10)
        n /= 10
    return result

def is_pandigital(n):
    d = digits(n)
    length = len(d)
    return sorted(d) == range(1, length + 1)

"""
result = 0
for n in xrange(987654321, 1, -1):
    if is_prime(n) and is_pandigital(n):
        result = n
        break
print result
"""

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

result = 0
for p in permutations('987654321', 7):
    p = int(''.join(p))
    if is_prime(p) and is_pandigital(p):
        result = p
        break
print result
