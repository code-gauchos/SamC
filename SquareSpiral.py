import turtle

turtle.bgcolor("black")
TurtlePen = turtle.Pen()

TurtlePen.pencolor("darkgreen")

for counter in range(100):
    TurtlePen.forward(counter)
    TurtlePen.left(90)