import math
import itertools

def find_factors(n):
  factors = set()
  factors.add(1)
  for i in xrange(2,int(math.sqrt(n))+1):
    if n % i == 0:
      factors.add(i)
      factors.add(n/i)

  return factors


abundant = set()
perfect = set()
deficient = set()

for i in xrange(1,30000):
  sum_for_i = sum(find_factors(i))
  if sum_for_i > i: abundant.add(i)
  elif sum_for_i == i: perfect.add(i)
  elif sum_for_i < i: deficient.add(i)

# it's correct up to here

numbers_that_are_the_sum_of_two_abundant_numbers = set()

# for combination in itertools.combinations(abundant, 2):
#   numbers_that_are_the_sum_of_two_abundant_numbers.add(combination[0] * combination[1])

abundant_list = list(abundant)

for i in xrange(len(abundant_list)):
  for j in xrange(i-1, len(abundant_list)):
    numbers_that_are_the_sum_of_two_abundant_numbers.add(abundant_list[i] * abundant_list[j])

numbers_less_than_28123 = set([i for i in xrange(1,28124)])

print len(numbers_less_than_28123)
print len(numbers_that_are_the_sum_of_two_abundant_numbers)

print sum(numbers_less_than_28123 - numbers_that_are_the_sum_of_two_abundant_numbers)
