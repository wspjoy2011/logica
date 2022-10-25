from turtle import *


line = Turtle()
line.left(90)
line.forward(200)
line.right(90)

pen = Pen()
pen.up()
pen.goto(line.xcor() + 10, line.ycor())


exitonclick()

