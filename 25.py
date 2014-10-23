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
def fib(n):
  if n <= 1: return n
  return fib(n-1) + fib(n-2)

n = 0
while True:
  ans = fib(n)
  if len(str(ans)) >= 1000:
    break
  n += 1

print ans
print n