# def next_collatz(n):
#   if n % 2 == 0:
#     return n/2
#   else:
#     return 3*n + 1

# def len_collatz(n):
#   count = 0
#   while n != 1:
#     n = next_collatz(n)
#     count += 1
#   return count

# max_collatz = 0
# max_i = 0

# for i in xrange(1000000):
#   l = len_collatz(i)
#   if l > max_collatz: 
#     max_collatz = l
#     max_i = i

import sys
sys.setrecursionlimit(10000000)

# http://www.quora.com/Is-there-a-decorator-that-does-memoization-built-in-to-Python
class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

@memoize
def len_collatz(n):
  if n == 1:
    return 1
  elif n % 2 == 0:
    return len_collatz(n/2) + 1
  else:
    return len_collatz(3*n+1) + 1

max_collatz = 0
max_i = 0

for i in xrange(1,1000000):
  l = len_collatz(i)
  if l > max_collatz: 
    max_collatz = l
    max_i = i

print max_i, max_collatz