from random import choice

f = open("five_lines.txt")
fives = f.readlines()
f.close()

for i in range(len(fives)):
	if fives[i] == "\n":
		fives.pop(i)
	else:
		fives[i] = fives[i].strip('\n')

f = open("seven_lines.txt")
sevens = f.readlines()
f.close()

for i in range(len(sevens)):
	if sevens[i] == "\n":
		sevens.pop(i)
	else:
		sevens[i] = sevens[i].strip('\n')

while True:
	line1 = choice(fives)
	line2 = choice(sevens)
	line3 = choice(fives)

	while line1 == line3:
		line3 = choice(fives)

	print
	print line1
	print line2
	print line3
	print

	cont = raw_input("Another? ")

	while len(cont) < 1:
		cont = raw_input("Another? ")
	
	if cont[0].lower() != "y":
		break

