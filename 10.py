# def primes(n):
#   seen = []
#   for i in xrange(2, n+1):
#     if all(map(lambda prime: i % prime, seen)):
#       seen.append(i)
  
#   return seen

# print sum(primes(2000000))

def primes_sieve(limit):
  limitn = limit+1
  not_prime = set()
  primes = []

  for i in range(2, limitn):
    if i in not_prime:
      continue

    for f in range(i*2, limitn, i):
      not_prime.add(f)

    primes.append(i)

  return primes

print sum(primes_sieve(2000000))