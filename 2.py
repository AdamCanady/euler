# def fib(n):
#   return n if n <= 1 else fib(n-1) + fib(n-2)

# sequence = []
# i = 0
# while i < 4000000:
#   i = fib(i) 

sequence = []
i, j = 0, 1
while j < 4000000:
  k = j
  j = i + j
  i = k
  sequence.append(j)

even_elements = []
for element in sequence:
  if element % 2 == 0:
    even_elements.append(element)

print sum(even_elements)

