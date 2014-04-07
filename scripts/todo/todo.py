# Get the file
# Get the lines
# While true: add items or remote items or print items
# Save file

f = open("mytodo.txt")
to_do_items = f.readlines()
f.close()

for i in range(len(to_do_items)):
	to_do_items[i] = to_do_items[i].strip('\n')

choice = "x"
while choice[0] != 'q':
	print "Do you want to [a]dd an item, [r]emove an item, [p] the list, or [q]uit?"
	choice = raw_input("a/r/p/q: ")
	if choice[0] == 'a':
		item = raw_input("Item: ")
		to_do_items.append(item)
	elif choice[0] == 'r':
		for i in range(len(to_do_items)):
			print i, to_do_items[i]
		remove = input("Remove #: ")
		try:
			to_do_items.pop(remove)
		except:
			print "Sorry, that didn't work."
	elif choice[0] == 'p':
		for item in to_do_items:
			print item
	elif choice[0] == 'q':
		print "Goodbye!"
	else:
		print "Huh?"

f = open("mytodo.txt", w)
for item in to_do_items:
	f.write(item + "\n")
f.close()


