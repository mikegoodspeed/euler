def divisors(n):
    divisors = []
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            divisors.append(i)
            other = n / i
            if other not in (n, i):
                divisors.append(other)
    return divisors

def sum_of_proper_divisors(n):
    count = 0
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            count += i
            other = n / i
            if other not in (n, i):
                count += other
    return count

abundant = [x for x in range(28124) if sum_of_proper_divisors(x) > x]

sum_abundant = []
for a in abundant:
    for b in abundant:
        sum_abundant.append(a + b)
sum_abundant = set(sum_abundant)

count = 0
for n in range(28124):
    if n not in sum_abundant:
        count += n
print count
