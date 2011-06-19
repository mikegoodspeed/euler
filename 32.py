def factor_pairs(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            yield (i, n / i)

def qualifies(n):
    for a, b in factor_pairs(n):
        if ''.join(sorted(repr(a) + repr(b) + repr(n))) == '123456789':
            print a, b, n
            return True
    return False

def main():
    print sum(i for i in range(10, 10000) if qualifies(i))

main()
