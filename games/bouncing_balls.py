from turtle import *
from random import random, randint, choice

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

window = Screen()
window.bgcolor('black')
window.title('Bouncing balls by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(lambda: window.bye(), 'Escape')
window.tracer(0)

balls = [Pen() for _ in range(20)]
direction = [-1, 1]

for ball in balls:
    ball.up()
    ball.speed(0)
    ball.shape('circle')
    ball.goto(randint(SCREEN_WIDTH // 2 * -1 + 20, SCREEN_WIDTH // 2 - 20),
              randint(SCREEN_HEIGHT // 2 * -1 + 20, SCREEN_HEIGHT // 2 - 20))
    ball.color(random(), random(), random())
    ball.delta_y = 0.1
    ball.delta_x = 0.2 * choice(direction)

gravity = 0.01


window.listen()

while True:
    window.update()

    for ball in balls:
        ball.goto(ball.xcor() + ball.delta_x, ball.ycor() - ball.delta_y)
        ball.delta_y += gravity
        if ball.ycor() < SCREEN_HEIGHT / 2 * -1 + 20:
            ball.delta_y *= -1

        if ball.xcor() > SCREEN_WIDTH / 2 - 20 or ball.xcor() < SCREEN_WIDTH / 2 * -1 + 20:
            ball.delta_x *= -1

    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 20:
                balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y


