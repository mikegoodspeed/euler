a = 1
b = 2
result = 0
while b <= 4000000:
    if b % 2 == 0:
        result += b
    a, b = b, b + a
print result
