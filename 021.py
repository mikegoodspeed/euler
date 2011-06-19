def sum_of_proper_divisors(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    return count

nums = range(10000)
divisors = map(sum_of_proper_divisors, nums)
result = []
for x in nums:
    y = divisors[x]
    if y < len(divisors) - 1 and divisors[y] == x and divisors[x] == y and x != y:
            result.append(x)
            result.append(y)
print sum(set(result))
