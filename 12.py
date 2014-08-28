import operator

def triangle_number_for(n):
  return reduce(operator.add, xrange(n+1))

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = 1
while True:
  tn = triangle_number_for(n)
  if len(factors(tn)) > 500:
    print tn
    exit()

  n += 1