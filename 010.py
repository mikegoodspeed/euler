def is_prime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

print sum([n for n in xrange(2, 2000000) if is_prime(n)])
