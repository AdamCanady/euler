# import re
# from fractions import Fraction
# from decimal import Decimal

# repeating = re.compile(r'(.+.+)(\1)+')

# max_repeating = ''
# max_d = 1

# for i in range(1,1001):
#   # denom = str(Fraction(1,i).decimal)
#   denom = str(Decimal(float(1)/i)).replace("0.","")
#   print denom

#   result = repeating.search(denom)
#   if not result: continue
#   repeating_part = str(result.group(1))
#   # print repeating_part, i
#   if len(repeating_part) > len(max_repeating):
#     max_repeating = repeating_part
#     max_d = i


# print max_repeating
# print max_d


def cycle_length(d):
    """Computes the length of the recurring cycle in the decimal representation
    of the rational number 1/d if any, 0 otherwise
    """

    if not isinstance(d, int) or d <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")

    rlist = []
    qlist_len = 0
    remainder = 1

    while remainder:
        remainder = remainder % d
        if remainder in rlist:
            return qlist_len - rlist.index(remainder)
        rlist.append(remainder)
        remainder *= 10
        qlist_len+=1

    return 0

max_d = 1
max_length = 0

for d in range(1,1001):
  this_length = cycle_length(d)
  if  this_length > max_length:
    max_length = this_length
    max_d = d

print max_d