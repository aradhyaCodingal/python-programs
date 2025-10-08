import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
number_of_sides=6
length=70
angle=360.0/number_of_sides
for i in range(number_of_sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()

