# import math

# def number_to_word(n):
#   output = ""
#   # thousands
#   if n >= 1000:
#     return "a thousand"

#   # hundreds
#   if n >= 100:
#     hundreds = math.floor(n/100)
#     if hundreds == 1: output += "a hundred"
#     else: output += number_to_word(hundreds) +" hundred"
#     n -= hundreds * 100
#     if n: output += " and "

#   # tens
#   if n >= 20:
#     if 100 > n and n >= 90: output += "ninety"
#     if 90 > n and n >= 80:  output += "eighty"
#     if 80 > n and n >= 70:  output += "seventy"
#     if 70 > n and n >= 60:  output += "sixty"
#     if 60 > n and n >= 50:  output += "fifty"
#     if 50 > n and n >= 40:  output += "fourty"
#     if 40 > n and n >= 30:  output += "thirty"
#     if 30 > n and n >= 20:  output += "twenty"
#     n -= n//10 * 10
#     if n: output += " "

#   # teens
#   if n > 10:
#     if n == 19: output += "nineteen"
#     if n == 18: output += "eighteen"
#     if n == 17: output += "seventeen"
#     if n == 16: output += "sixteen"
#     if n == 15: output += "fifteen"
#     if n == 14: output += "fourteen"
#     if n == 13: output += "thirteen"
#     if n == 12: output += "twelve"
#     if n == 11: output += "eleven"
#     return output

#   if n == 10: 
#     output += " ten"
#     return output

#   # ones
#   ones = n % 10
#   if ones == 9: output += "nine"
#   if ones == 8: output += "eight"
#   if ones == 7: output += "seven"
#   if ones == 6: output += "six"
#   if ones == 5: output += "five"
#   if ones == 4: output += "four"
#   if ones == 3: output += "three"
#   if ones == 2: output += "two"
#   if ones == 1: output += "one"

#   return output

# total = 0
# for i in range(1,1001):
#   num = number_to_word(i).replace(" ","")
#   # print num
#   total += len(num)

# print total

# 1-9
s = 36

# 10-19
s += 70

# 20-99
s += 10*(6+6+5+5+5+7+6+6) + 8*36 

# 100-999
s += 100*36 + 9*854 + 9*7 + 9*99*10

# 1000
s += 11

print s