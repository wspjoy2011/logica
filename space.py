from turtle import *
from random import randint


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.color('white')
        self.velocity = 0
        self.up()


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.lasers = []
        self.velocity = 0.01
        self.angle = 2
        self.shape('spaceship')

    def get_velocity(self):
        return self.velocity

    def up_velocity(self):
        if self.velocity <= 0.03:
            self.velocity += 0.01

    def check_border(self):
        if self.xcor() > SCREEN_WIDTH // 2:
            self.goto(-SCREEN_WIDTH // 2, self.ycor())
        elif self.xcor() < -SCREEN_WIDTH // 2:
            self.goto(SCREEN_WIDTH // 2, self.ycor())

        if self.ycor() > SCREEN_HEIGHT // 2:
            self.goto(self.xcor(), -SCREEN_HEIGHT // 2)
        elif self.ycor() < -SCREEN_HEIGHT // 2:
            self.goto(self.xcor(), SCREEN_HEIGHT // 2)

    def turn_left(self):
        self.left(self.angle)

    def turn_right(self):
        self.right(self.angle)

    def shot(self):
        self.lasers.append(Laser())


class Enemy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.hideturtle()
        self.goto(randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2),
                  randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2))
        self.showturtle()
        self.velocity = 0.005
        self.color('red')
        self.shape('spaceship')


    def move(self):
        self.setheading(self.towards(player.xcor(), player.ycor()))
        self.forward(self.velocity)


class Laser(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.shape('square')
        self.shapesize(0.25, 0.75, None)
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        self.showturtle()
        self.velocity = 0.05

    def move(self):
        self.forward(self.velocity)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.bgcolor('black')
window.title('Space game by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
player_vertices = ((0, 15), (-15, 0), (-18, 5), (-18, -5), (0, 0), (18, -5), (18, 5), (15, 0))
window.register_shape('spaceship', player_vertices)
window.tracer(0)

player = Player()
enemies = [Enemy() for _ in range(3)]

window.onkey(player.up_velocity, 'Up')
window.onkey(player.shot, 'space')
window.onkeypress(player.turn_left, 'Left')
window.onkeypress(player.turn_right, 'Right')
window.listen()

while True:
    window.update()
    if player.lasers:
        for laser in player.lasers:
            laser.move()
            # if laser.distance(enemy) < 15:
            #     enemy.hideturtle()
    for enemy in enemies:
        enemy.move()
    player.forward(player.get_velocity())
    player.check_border()
