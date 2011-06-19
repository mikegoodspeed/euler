def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def rotations(n):
    yield n
    n = str(n)
    for i in range(len(n) - 1):
        n = n[1:] + n[0]
        yield int(n)

def is_circular(n):
    for i in rotations(n):
        if not is_prime(i):
            return False
    return True

print len([i for i in range(2, 1000000) if is_circular(i)])
