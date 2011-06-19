def num_factors(n):
    count = 0
    for i in range(1, int(n ** .5)):
        if n % i == 0:
            count += 2
    return count

i = 0
n = 1
f = 0
while f < 500:
    i += n
    f = num_factors(i)
    n += 1
print i
