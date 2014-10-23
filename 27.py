num_odds_to_skip = 0
odd_count = 0

corners = set()

for i in range(2,1001**2):

  if odd_count % 4 == 0:
    num_odds_to_skip += 1

  if i % 2 == 1:
    odd_count += 1