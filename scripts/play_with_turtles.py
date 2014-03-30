import turtle

turtle.showturtle()
turtle.turtlesize(1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while True:

    for color in colors:
        turtle.color(color)
        turtle.stamp()
        turtle.forward(10)
        turtle.left(10)

# add some colors
# add something that isn't a color?
# change forward
# change left
# does right work?
# Remove while True:
