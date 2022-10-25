from turtle import *
from random import choice

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.up()
        self.color('white')


class Paddle(Sprite):
    def __init__(self, start_x, speed):
        Sprite.__init__(self)
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(start_x, 0)
        self.delta_y = speed
        self.width = 20
        self.height = 100

    def move_up(self):
        y = self.ycor()
        if y + self.height // 2 < SCREEN_HEIGHT // 2:
            self.goto(self.xcor(), y + self.delta_y)

    def move_down(self):
        y = self.ycor()
        if y - self.height // 2 > -SCREEN_HEIGHT // 2:
            self.goto(self.xcor(), y - self.delta_y)


class Ball(Sprite):
    directions = (-1, 1)

    def __init__(self):
        Sprite.__init__(self)
        self.shape('circle')
        self.delta_x = 0.1 * choice(self.directions)
        self.delta_y = 0.1 * choice(self.directions)

    def move(self):
        self.goto(self.xcor() + self.delta_x, self.ycor() + self.delta_y)
        window.update()

    def check_border(self):
        x = self.xcor()
        y = self.ycor()
        if x < -SCREEN_WIDTH // 2 + 10 or x > SCREEN_WIDTH // 2 - 10:
            self.delta_x *= -1

        if y < -SCREEN_HEIGHT // 2 + 10 or y > SCREEN_HEIGHT // 2 - 10:
            self.delta_y *= -1

    def check_paddle(self, paddle):
        x = self.xcor()
        y = self.ycor()

        if paddle.xcor() - paddle.width < x < paddle.xcor() + paddle.width and \
                paddle.ycor() - paddle.height // 2 < y < paddle.ycor() + paddle.height // 2:
            self.delta_x *= -1


window = Screen()
window.bgcolor('black')
window.title('Pong by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.tracer(0)

computer = Paddle(SCREEN_WIDTH // 2 - 50, 7)
player = Paddle(-SCREEN_WIDTH // 2 + 50, 3)
ball = Ball()


window.onkeypress(player.move_up, 'Up')
window.onkeypress(player.move_down, 'Down')
window.listen()
while True:
    ball.move()
    ball.check_border()
    ball.check_paddle(player)
    ball.check_paddle(computer)
    if computer.ycor() + computer.height // 2 > ball.ycor():
        computer.move_down()
    elif computer.ycor() - computer.height // 2 < ball.ycor():
        computer.move_up()
