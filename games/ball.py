from turtle import *


def check_border(x, y):
    global touch
    if y < -SCREEN_HEIGHT // 2 + 10 or y > SCREEN_HEIGHT // 2 - 10:
        ball.delta_y *= -1
        touch += 1
        print(touch)
    if x < -SCREEN_WIDTH // 2 + 10 or x > SCREEN_WIDTH // 2 - 10:
        ball.delta_x *= -1
        touch += 1
        print(touch)


touch = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.title('Ball game by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')

ball = Turtle()
ball.delta_y = 2
ball.delta_x = 1
ball.speed(0)
ball.hideturtle()
ball.up()
ball.color('blue')
ball.shape('circle')
ball.goto(0, 200)
ball.showturtle()

window.listen()
while True:
    x = ball.xcor()
    y = ball.ycor()
    check_border(x, y)
    ball.goto(x - ball.delta_x, y - ball.delta_y)
