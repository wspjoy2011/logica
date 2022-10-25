from turtle import *
from random import randint, random
from tkinter import messagebox


def make_settings(item, item_shape, item_color):
    item.shape(item_shape)
    item.color(item_color)
    item.hideturtle()
    item.up()
    item.goto(-SCREEN_WIDTH / 2, randint(-SCREEN_HEIGHT // 2,
                                         SCREEN_HEIGHT // 2))
    item.showturtle()


def check_finish(item):
    x = item.xcor()
    if x > SCREEN_WIDTH // 2 - 20:
        messagebox.showinfo('Winner', f'{item.name.title()} is winner!')
        window.bye()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

bob = Turtle()
bob.name = 'bob'

tom = Pen()
tom.name = 'tom'

jerry = Turtle()
jerry.name = 'jerry'

items = [bob, tom, jerry]
for item in items:
    make_settings(item, 'turtle', (random(), random(), random()))


for _ in range(150):
    for item in items:
        check_finish(item)
        item.forward(randint(1, 10))


exitonclick()
