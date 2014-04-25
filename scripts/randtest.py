from random import randint

totals = {}

for i in range(1000):
  n = randint(1, 10)
  if n in totals:
    totals[n] += 1
  else:
    totals[n] = 1

for num in totals:
  print "{num}:\t{total}".format(num=num, total=totals[num])
