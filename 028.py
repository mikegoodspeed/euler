def corners(n):
    if n == 0:
        return 1
    size = 2 * n + 1
    corner = size ** 2
    count = 0
    for i in range(4):
        count += corner
        corner -= size - 1
    return count

rows = (1001 - 1) / 2
count = 0
for i in range(rows + 1):
    count += corners(i)
print count
