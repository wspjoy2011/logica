from turtle import *

t = 0
tstep = 0.25  # seconds
delx = 2  # uniform motion in x axis
g = -1  # fixed accel (downwards)
yvel = 20  # initial vel in y
y = 0  # y position

penup()
goto(-100, 0)
pendown()
color("green")
forward(150)
right(90)
forward(100)
penup()
goto(0, 0)

pendown()
color("blue")

print("run the simulation for 50 seconds ")
while (t < 50):
    t = t + tstep
    x = t * delx
    yvel = yvel + g * tstep  # change in y vel = accel * time interval
    y = y + yvel * tstep  # change in y posn = vel + time interval

    goto(x, y)
    dot(2, "blue")  # draw dot at current position

print("final y position is " + str(y) + " m")
write(" python rules! ")
print("that's all folks")
exitonclick()