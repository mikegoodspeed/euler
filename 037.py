def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int((n ** .5) + 1)):
        if n % i == 0:
            return False
    return True

def ltrunc_int(n):
    n = repr(n)[1:]
    while n:
        yield int(n)
        n = n[1:]

def rtrunc_int(n):
    n = repr(n)[:-1]
    while n:
        yield int(n)
        n = n[:-1]

count = 0
i = 10
result = 0
while count < 11:
    if is_prime(i):
        qualifies = True
        truncs = list(ltrunc_int(i)) + list(rtrunc_int(i))
        for j in truncs:
            if not is_prime(j):
                qualifies = False
                break
        if qualifies:
            result += i
            count += 1
    i += 1
print result
