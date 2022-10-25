from turtle import *
from random import randint, random
from tkinter import messagebox


def make_turtle_settings(item):
    item.speed(0)
    item.hideturtle()
    item.up()
    item.goto(-SCREEN_WIDTH // 2 + 10,
              randint(-SCREEN_HEIGHT // 2 + 10, SCREEN_HEIGHT // 2 -10))
    item.showturtle()
    item.shape('turtle')
    item.color((random(), random(), random()))


def check_finish(item):
    x = item.xcor()
    if x > SCREEN_WIDTH // 2 - 10:
        messagebox.showinfo('Winner', f'{item.name.title()} is winner!')
        window.bye()


def move_turtle(item):
    x = item.xcor()
    y = item.ycor()
    item.goto(x + randint(1, 20), y)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.title('Turtles race!')

turtles = [Turtle() for _ in range(5)]
names = ['tom', 'jerry', 'bob', 'john', 'jane']

for i in range(len(turtles)):
    make_turtle_settings(turtles[i])
    turtles[i].name = names[i]


while True:
    for item in turtles:
        check_finish(item)
        move_turtle(item)
