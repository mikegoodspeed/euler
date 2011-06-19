small = """3
7 4
2 4 6
8 5 9 3"""
big ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = big
elements = [map(int, line.split(' ')) for line in data.split('\n')]

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args[1:] not in cache:
            cache[args[1:]] = func(*args)
        return cache[args[1:]]
    return wrapper

@memoize
def find_max(grid, row, col):
    result = grid[row][col]
    if row == len(grid) - 1:
        return result
    return result + max(find_max(grid, row + 1, col), find_max(grid, row + 1, col + 1))

print find_max(elements, 0, 0)
