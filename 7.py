from itertools import islice

def primes(n):
  seen = []
  for i in xrange(2, n+1):
    if all(map(lambda prime: i % prime, seen)):
      seen.append(i)
      yield i

print next(islice(primes(1000000000), 10000, 10001))