a , b = 1, 1
x = int('1' + ('0' * 999))
i = 2
while b < x:
    a, b = b, a + b
    i += 1
print i
