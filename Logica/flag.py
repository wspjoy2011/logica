from timeit import timeit


def check_dict():
    return branch

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('ham', check_dict()))

# color = ['red', 'blue', 'green']

class Arr(list):
    def __init__(self, name, count = -1):
        self.name = name
        self.count = count
    def next_item(self):
        if self.count >= len(self) -1: self.count = -1
        self.count += 1
        return self[self.count]


color = Arr('Color choice')
color.append('red')
color.append('blue')
color.append('green')
print(color)
print(color.name)
print(color.next_item())
print(color.next_item())
print(color.next_item())
print(color.next_item())
def return_double(x):
    return x**x

arr = [return_double]
print(arr[0](2))
print(1 == True)


def func(): ...
print(0.1+0.2)
print(isinstance(0, bool))

arr = ['sdf','sfghgh, sdfds', 0]
for item in arr:
    print(item, id(item))

print(type(' '.join([str(i) for i in range(1, 101)])))
search_list = list(range(100000))

import turtle
from turtle import *

# screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()

# Orange Rectangle
# white rectangle
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()

# Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

# to hold the
# output window
turtle.done()