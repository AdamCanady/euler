for a in xrange(1,1000):
  for b in xrange(a,1000):
    for c in xrange(1,1000):
      if a**2 + b**2 == c**2 and a+b+c == 1000:
        print a*b*c
        exit()