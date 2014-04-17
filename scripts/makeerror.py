def get_name():
	name = raw_input("Name: ")
	return name

def get_age():
	age = input("Age: ")
	return age

def print_stuff(name, age):
	print "Hi, " + name + ", who is " + age + "."

def main():
	name = get_name()
	age = get_age()
	print_stuff(name, age)    

if __name__ == '__main__':
	main()