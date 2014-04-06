from random import choice

f = open("five_lines.txt")
fives = f.readlines()
f.close()

f = open("seven_lines.txt")
sevens = f.readlines()
f.close()

while True:
	line1 = choice(fives)
	line2 = choice(sevens)
	line3 = choice(fives)

	print line1
	print line2
	print line3

	cont = raw_input("Another? ")
	if cont[0].lower() != "y":
		break

