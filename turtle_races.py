from turtle import *
from random import random, randint
from tkinter import messagebox
from time import sleep


def countdown():
    count = 3
    pen_countdown = Pen()
    pen_countdown.color('red')
    pen_countdown.hideturtle()
    pen_countdown.goto(0, 0)
    for i in range(count):
        pen_countdown.write(count, align='center', font=('Arial', 20, 'bold'))
        sleep(1)
        count -= 1
        pen_countdown.clear()


def game():
    while True:
        window.update()
        for turtle in turtles:
            if turtle.xcor() > finish_x:
                # messagebox.showinfo('winner', f'winner is {turtle.name}')
                pen.up()
                pen.goto(0, 0)
                pen.write(f'Winner is {turtle.name}', align='center', font=('Arial', 16, 'bold'))
                window.exitonclick()
            move_turtle(turtle)




def make_turtle_settings(turtle, turtle_color, y, name):
    turtle.up()
    turtle.name = name
    turtle.hideturtle()
    turtle.speed(0)
    turtle.color(turtle_color)
    turtle.shape('turtle')
    turtle.goto(start_x, y)
    turtle.showturtle()


def draw_start():
    pen.hideturtle()
    pen.up()
    pen.width(5)
    pen.goto(start_x + 20, -SCREEN_HEIGHT // 2 + 50)
    pen.left(90)
    pen.down()
    pen.forward(SCREEN_HEIGHT - 75)


def draw_finish():
    pen.up()
    pen.goto(finish_x, pen.ycor())
    pen.left(90)
    pen.right(90)
    pen.down()
    pen.forward(-SCREEN_HEIGHT + 75)


def move_turtle(turtle):
    turtle.forward(randint(1, 20) // 15)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
start_y = SCREEN_HEIGHT // 2 - 50
start_x = -300
finish_x = SCREEN_WIDTH //2 - 100


window = Screen()
window.title('Turtle races')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

pen = Pen()
countdown()
draw_start()
draw_finish()


turtles = [Turtle() for i in range(10)]
number = 1

for turtle in turtles:
    make_turtle_settings(turtle, (random(), random(), random()), start_y, number)
    number += 1
    start_y -= 50


window.listen()
game()

