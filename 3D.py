from turtle import *


def make_block_settings(block, y, size_x, block_color):
    block.up()
    block.goto(0, y)
    block.shape('square')
    block.shapesize(1.0, size_x)
    block.color(block_color)


window = Screen()
window.tracer(0)

block_red = Turtle()
block_blue = Turtle()
block_green = Turtle()

make_block_settings(block_red, 0, 12.0, 'red')
make_block_settings(block_blue, 20, 10.0, 'blue')
make_block_settings(block_green, 40, 8.0, 'green')
angle = 0.1

blocks = [block_green, block_blue, block_red]
while True:
    window.update()
    for block in blocks:
        block.setheading(angle)
    angle += 0.1
