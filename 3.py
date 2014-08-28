# def factors(n):
#   results = []
#   for i in range(1,n/2+1):
#     if n % i == 0:
#       results.append(i)
#   return results

# # print factors(4), factors(8), factors(18)

# def primes_up_to(n):
#   a = [True] * n
#   a[0] = False
#   a[1] = False

#   for (i, result) in enumerate(a):
#     if isprime:
#       yield i
#       for m in xrange(i*i, n, i):
#         a[m] = False


# def primes_sieve(limit):
#     limitn = limit+1
#     not_prime = set()
#     primes = []

#     for i in range(2, limitn):
#         if i in not_prime:
#             continue

#         for f in range(i*2, limitn, i):
#             not_prime.add(f)

#         primes.append(i)

#     return primes

# for i in primes_sieve(600851475143/2+1):
#   print i

# # f = factors(600851475143)

# http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
            print n, d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            print "h"
            break
    return factors

pfs = prime_factors(600851475143)
print pfs
largest_prime_factor = max(pfs)
print largest_prime_factor