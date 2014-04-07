# Get the file
# Get the lines
# While true: add items or remote items or print items
# Save file

f = open("mytodo.txt")
to_do_items = f.readlines()
f.close()

choice = "x"
while choice[0] != 'q':
	print "Do you want to [a]dd an item, [r]emove an item, [p] the list, or [q]uit?"
	choice = raw_input("a/r/p/q: ")
	if choice[0] == 'a':
		item = raw_input("Item: ")
		to_do_items.append(item)
	elif choice[0] == 'r':
		

