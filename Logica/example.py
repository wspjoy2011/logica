import turtle as t
import random

pen = t.Turtle()
colors = ['red', 'green', 'blue', 'cyan']
pen.speed(0)

def draw_square():
    for side in range(4):
        pen.forward(100)
        pen.right(90)
        for side in range(4):
            pen.forward(50)
            pen.right(90)

pen.penup()
pen.back(20)
pen.pendown()

for square in range(80):
    pen.color(random.choice(colors))
    draw_square()
    pen.forward(5)
    pen.left(5)

pen.hideturtle()