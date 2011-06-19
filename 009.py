import sys

def is_triplet(a, b, c):
    if a > b or a > c or b > c:
        return False
    return a ** 2 + b ** 2 == c ** 2

for a in xrange(1, 1000):
    for b in xrange(1, 1000):
        for c in xrange(1, 1000):
            if a + b + c == 1000 and is_triplet(a, b, c):
                print a, b, c, a * b * c
                sys.exit(0)
