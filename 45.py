def triangle(n):
    return (n ** 2 + n) / 2

def pentagonal(n):
    return (3 * n ** 2 - n) / 2

def hexagonal(n):
    return (2 * n ** 2 - n)

#n = 3n - 2 = 4n - 3

t = set([triangle(x) for x in range(1, 1000000)])
p = set([pentagonal(x) for x in range(1, 1000000)])
h = set([hexagonal(x) for x in range(1, 1000000)])

for x in t:
    if x in p and x in h:
        print x
