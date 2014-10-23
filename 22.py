names = [name.replace('"', "") for name in open('p022_names.txt','r').read().split(",")]

total = 0

for i, name in enumerate(sorted(names)):
  name_score = 0

  for letter in name:
    letter_score = ord(letter) - 64
    name_score += letter_score

  name_score *= i+1

  total += name_score

print total