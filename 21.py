import math

def find_factors(n):
  factors = set()
  factors.add(1)
  for i in xrange(2,int(math.sqrt(n))+1):
    if n % i == 0:
      factors.add(i)
      factors.add(n/i)

  return factors

d = {}

for i in xrange(1,10001):
  d[i] = sum(find_factors(i))

amicable_numbers = set()

for key, value in d.items():
  if d.get(value, "") == key and key != value:
    amicable_numbers.add(key)

print amicable_numbers

print sum(amicable_numbers)