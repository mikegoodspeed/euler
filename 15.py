def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def routes(width, height):
    if width + height in (0, 1):
        return width + height
    count = 0
    if width > 0:
        count += routes(width - 1, height)
    if height > 0:
        count += routes(width, height - 1)
    return count

print routes(20, 20)
