import turtle
import time

turtlePen = turtle.Pen()
turtlePen.speed(1000)


turtle.circle(40)

counter=0

turtlePen.goto(-10,5)


while counter<=8:
    turtlePen.forward(40)
    turtlePen.left(45)
    counter+=1

time.sleep(10)