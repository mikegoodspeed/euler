factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
result = 0
for i in xrange(10, 100000):
    if i == sum([factorial[n] for n in map(int, str(i))]):
        result += i
print result
