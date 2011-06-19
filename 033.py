def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def divisors(n):
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            yield i
            other = n / i
            if other != i:
                yield other

def digits(n):
    while n:
        yield n % 10
        n /= 10

def intersect(a, b):
     return list(set(a) & set(b))

for a in range(10, 100):
    x = list(reversed(list(digits(a))))
    for b in range(a + 1, 100):
        y = list(reversed(list(digits(b))))
        intersection = intersect(x, y)
        if not intersection:
            continue
        print a, b, intersection, gcd(a, b)


b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]

print intersect(b1, b2)