def factors(n):
    yield 1
    i = 2
    original = n
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            yield i
            n = n / i
            limit = n**0.5
        else:
            i += 1
    if n > 1:
        yield n
        if n != original:
            yield original

num_factors = 1
result = 1
count = 1
while num_factors <= 20:
    count += 1
    result += count
    num_factors = len(list(factors(result)))
print result

