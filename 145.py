import time

def print_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print func.func_name, time.time() - start
    return wrapper

@print_time
def brute_force():
    odd = set([1, 3, 5, 7, 9])
    count = 0
    for n in xrange(1, 1000000):
        if n % 10 == 0:
            continue
        n = n + int(str(n)[::-1])
        if len(str(n)) % 2 != 0:
            continue
        #temp = n
        is_odd = True
        while n > 0:
            d = n % 10
            if d not in odd:
                is_odd = False
                break
            n /= 10
        if is_odd:
            count += 1
            #print '%s\t%s\t%s\t%s' % (count, temp, temp + int(str(temp)[::-1]), len(str(temp + int(str(temp)[::-1]))) )
    print count

brute_force()
