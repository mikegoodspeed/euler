def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

result = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        test = a * b
        if is_palindrome(test) and test > result:
            result = test
print result
