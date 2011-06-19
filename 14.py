"""
#50 seconds
def series_len(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n= 3 * n + 1
        count += 1
    return count

result, l = 0, 0
for n in range(1, 1000000):
    test = series_len(n)
    if test > l:
        result, l = n, test
print result
"""

# 3 seconds
def series_len(n, cache={1:1}):
    orig = n
    count = 1
    while n not in cache:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1
    count += cache[n] - 1
    cache[orig] = count
    return count

cache = {1:1}
result, l = 0, 0
for n in range(1, 1000000):
    test = series_len(n)
    if test > l:
        result, l = n, test
print result
