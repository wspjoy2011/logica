from turtle import *
from random import randint


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.up()
        self.shapesize(3, 3)


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape('circle')
        self.color('blue')
        self.goto(0, -300)


class Enemy(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.shape('square')
        self.color('red')
        self.goto(x, y)


class FinalPoint(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape('triangle')
        self.color('green')
        self.goto(0, 300)


window = Screen()
window.setup(800, 800)

player = Player()

enemy1 = Enemy(randint(-370, 370), randint(-370, 370))
enemy2 = Enemy(randint(-370, 370), randint(-370, 370))

final_point = FinalPoint()


window.mainloop()