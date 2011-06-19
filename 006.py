def sum_of_the_squares(numbers):
    return sum([i ** 2 for i in numbers])

def square_of_the_sum(numbers):
    return sum([i for i in numbers]) ** 2

numbers = range(1, 101)
print square_of_the_sum(numbers) - sum_of_the_squares(numbers)
