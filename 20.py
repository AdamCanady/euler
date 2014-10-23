n = 100
i = 1

while n > 0:
  i *= n
  n -= 1

s = 0
str_i = str(i)
for j in str_i:
  s += int(j)

print s