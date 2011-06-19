def is_prime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

i = 1
primes = 0
while primes < 10001:
    i += 1
    if is_prime(i):
        primes += 1
print i
