# found = False
# n = 0
# numbers = range(1,21)

# while not found:
#   results = set()
#   for i in numbers:
#     results.add(n % i == 0)
#   if True not in results:
#     found = True
#   else:
#     n += 1

# print n

# import operator
# from fractions import gcd

# numbers = range(1,21)
# product = reduce(operator.mul, numbers)

# # print product, numbers

# def gcd_list(l):
#   return reduce(gcd, l)

# # print product, gcd_list(numbers)

from itertools import count, takewhile

def primes(n):
  seen = []
  for i in xrange(2, n+1):
    if all(map(lambda prime: i % prime, seen)):
      seen.append(i)
      yield i

def smallest(n):
  result = 1
  for prime in primes(n):
    bprime = max(takewhile(lambda x:x <= n, (prime ** c for c in count(1))))
    result *= bprime

  return result

print smallest(20)