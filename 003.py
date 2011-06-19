def factors(n):
    yield 1
    i = 2
    limit = n ** 0.5
    while i <= limit:
        if n % i == 0:
            yield i
            n = n / i
            limit = n ** 0.5
        else:
            i += 1
    if n > 1:
        yield n

def is_prime(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

print max([f for f in factors(600851475143) if is_prime(f)])
