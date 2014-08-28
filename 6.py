import operator

numbers = range(1,101)
sum_of_squares = sum(map(lambda x: x**2, numbers))
square_of_sum = reduce(operator.add, numbers)**2

print square_of_sum - sum_of_squares