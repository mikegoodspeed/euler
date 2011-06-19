import time

def print_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print func.func_name, time.time() - start
    return wrapper


def is_palindrome(n):
    n = repr(n)
    start = 0
    end = len(n) - 1
    while start <= end:
        if n[start] != n[end]:
            return False
        start += 1
        end -= 1
    return True

def binary(n):
    digs = []
    while n:
        digs.append(n % 2)
        n /= 2
    digs.reverse()
    return ''.join(map(str, digs))

@print_time
def main():
    result = 0
    for n in xrange(1, 1000000, 2):
        if is_palindrome(n) and is_palindrome(binary(n)):
            result += n
    print result

main()
