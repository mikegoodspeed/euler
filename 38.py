def num_digits(n):
    count = 0
    while n:
        n /= 10
        count += 1
    return count

def digits(n):
    result = []
    while n:
        result.append(n % 10)
        n /= 10
    return result

def is_pandigital(n):
    d = digits(n)
    length = len(d)
    return sorted(d) == range(1, length + 1)

def main():
    result = []
    for i in xrange(1, 10000):
        cp = 0
        cp_digits = 0
        n = 1
        while cp_digits < 9:
            new = n * i
            cp *= 10 ** num_digits(new)
            cp += new
            cp_digits = num_digits(cp)
            n += 1
        if cp_digits == 9 and is_pandigital(cp):
            result.append(cp)
    print max(result)

main()
