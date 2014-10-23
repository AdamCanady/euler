import itertools

digits = [str(i) for i in range(0,10)]

print "".join(next(itertools.islice(itertools.permutations(digits), 999999, 999999 + 1)))