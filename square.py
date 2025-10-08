import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
square=turtle.Turtle()
number_of_sides=4
length=70
angle=360.0/number_of_sides
for i in range(number_of_sides):
    square.forward(length)
    square.right(angle)
turtle.done()

