import turtle

turtle.bgcolor("black")
TurtlePen = turtle.Pen()

TurtlePen.pencolor("red")

for counter in range(100):
    TurtlePen.forward(counter)
    TurtlePen.left(45)