import turtle
import math


class DrawCircle():

    def __init__(self, color):
        self.name = turtle.Turtle()
        self.color = color
        self.name.speed(0)

    def draw(self):
        self.name.begin_fill()
        self.name.color(self.color[0], self.color[1])
        for i in range(1000):
            self.name.forward(math.cos(i/10)*60+i%2)
            self.name.left(20)
        self.name.end_fill()

    def go_to(self, coord):
        self.name.up()
        self.name.goto(coord[0], coord[1])
        self.name.down()

    def change_color(self, color):
        self.color = color


bob = DrawCircle(['red', 'yellow'])
bob.draw()
bob.go_to([250, 100])
bob.change_color(['blue', 'green'])
bob.draw()

alice = DrawCircle(['cyan', 'purple'])
alice.go_to([-150, -350])
alice.draw()
# go_to([250, 100])
# draw(['red', 'yellow'])

turtle.done()
