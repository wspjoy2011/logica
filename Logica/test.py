from turtle import *
from random import randint

SCREEN_SIZE = 800

window = Screen()
window.setup(SCREEN_SIZE, SCREEN_SIZE)

ball = Turtle()
ball.color('red')
ball.shape('circle')
ball.shapesize(2, 2)
ball.up()
delta_x = 1
delta_y = 1
ball.goto(randint(-SCREEN_SIZE / 2, SCREEN_SIZE / 2), randint(-SCREEN_SIZE / 2, SCREEN_SIZE / 2))

while True:
    ball.goto(ball.xcor() + delta_x, ball.ycor() + delta_y)
    if ball.xcor() > SCREEN_SIZE // 2 or ball.xcor() < -SCREEN_SIZE // 2:
        delta_x *= -1
    if ball.ycor() > SCREEN_SIZE // 2 or ball.ycor() < -SCREEN_SIZE // 2:
        delta_y *= -1