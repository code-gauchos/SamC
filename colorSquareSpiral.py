import turtle

turtle.bgcolor("black")
TurtlePen = turtle.Pen()
TurtlePen.speed(100)
#hi sam whats up
COLORS = ["red", "yellow", "blue", "purple", "pink", "darkgreen"]
#sam
for counter in range(600):
    TurtlePen.pencolor(COLORS[counter%6])
    TurtlePen.forward(counter)
    TurtlePen.left(30)
    TurtlePen.forward(counter)
    TurtlePen.left(30)
    