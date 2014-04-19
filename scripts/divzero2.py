num1 = input("First number: ")
num2 = input("Second number: ")
try:
  print "Result:", num1 / num2
except ZeroDivisionError:
  print "Result: Infinity"
