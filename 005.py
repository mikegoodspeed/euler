def is_answer(num):
    for i in range(20, 1, -1):
        if num % i != 0:
            return False
    return True

result = 20
while not is_answer(result):
    result += 20
print result
