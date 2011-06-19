def same_digits(x, *args):
    x = sorted(repr(x))
    for arg in args:
        if x != sorted(repr(arg)):
            return False
    return True

def main():
    finished = False
    x = 0
    while not finished:
        x += 1
        if same_digits(x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x):
            finished = True
    print x

main()
