palindromes = set()
for i in range(1,1000):
  for j in range(1,1000):
    number = str(i*j)
    if len(number) % 2 == 0:
      # even
      first_half = number[:len(number)/2]
      second_half = number[len(number)/2:]
    else:
      first_half = number[:len(number)/2]
      second_half = number[len(number)/2+1:]

    first_half_backwards = first_half[::-1]

    if first_half_backwards == second_half:
      palindromes.add(int(number))

    # print i, j, number, first_half_backwards, second_half

largest = max(palindromes)
# print palindromes
print largest