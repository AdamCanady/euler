
# def make_grid():
#   return [[False for j in xrange(20)] for i in xrange(20)]

# for i in range(20):

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


end_count = 0
@memoize
def paths(rows_left, columns_left):
  if not rows_left and not columns_left:
    global end_count
    end_count += 1 
    return 1
  elif not rows_left:
    # print rows_left, columns_left, "right"
    return paths(0, columns_left-1)
  elif not columns_left:
    # print rows_left, columns_left, "down"
    return paths(rows_left-1, 0)
  else:
    # print rows_left, columns_left, "down and right"
    return paths(rows_left-1, columns_left) + paths(rows_left, columns_left-1)

print paths(20,20)

print end_count
