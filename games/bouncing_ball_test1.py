from turtle import *


def check_ground():
    y = ball.ycor()
    x = ball.xcor()

    if y < -SCREEN_HEIGHT // 2:
        ball.delta_y *= -1

    if x > SCREEN_WIDTH // 2 or x < -SCREEN_WIDTH // 2:
        ball.delta_x *= -1

def move_ball():
    y = ball.ycor()
    x = ball.xcor()
    ball.goto(x + ball.delta_x, y - ball.delta_y)
    ball.delta_y += gravity


def move_paddle_right():
    x = paddle.xcor()
    y = paddle.ycor()
    paddle.goto(x + 5, y)


def move_paddle_left():
    x = paddle.xcor()
    y = paddle.ycor()
    paddle.goto(x - 5, y)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.title('Bouncing ball!')
window.onkeypress(move_paddle_right, 'Right')
window.onkeypress(move_paddle_left, 'Left')

ball = Turtle()
ball.speed(0)
ball.hideturtle()
ball.up()
ball.goto(0, 200)
ball.color('blue')
ball.shape('circle')
ball.showturtle()
ball.delta_y = 2
ball.delta_x = 2
ball.width = 20
ball.height = 20
gravity = 0.1

paddle = Turtle()
paddle.width = 80
paddle.height = 10
paddle.hideturtle()
paddle.up()
paddle.goto(0, -250)
paddle.shape('square')
paddle.shapesize(0.5, 4.0, None)
paddle.showturtle()

window.listen()
while True:
    check_ground()
    move_ball()

    if ball.xcor() < paddle.xcor() + paddle.width and \
    ball.xcor() + ball.width > paddle.xcor() and \
    ball.ycor() < paddle.ycor() + paddle.height and \
    ball.height + ball.ycor() > paddle.ycor():
        ball.sety(ball.ycor() + 10)
        ball.delta_y *= -1