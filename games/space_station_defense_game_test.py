from turtle import *
import math


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.velocity = 0
        self.speed(0)


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.velocity = 0.05
        self.angle = 5
        self.degrees = 0
        self.missiles = []
        self.up()
        self.color('white')
        self.shape('spaceship')

    def check_border(self):
        x = self.xcor()
        y = self.ycor()

        if x < -SCREEN_WIDTH // 2 - 90 or x > SCREEN_WIDTH // 2 + 90:
            if x < 0:
                x = SCREEN_WIDTH // 2 + 60
            elif x > 0:
                x = -SCREEN_WIDTH // 2 - 60

        if y < -SCREEN_HEIGHT // 2 - 90 or y > SCREEN_HEIGHT // 2 + 90:
            if y < 0:
                y = SCREEN_HEIGHT // 2 + 60
            else:
                y = -SCREEN_HEIGHT // 2 - 60

        self.goto(x, y)

    def get_heading(self, x2, y2):
        tmp = math.atan2(-y2, -x2)
        self.degrees = round((tmp + math.pi) * 360 / (2.0 * math.pi))
        print(self.degrees)

    def rotate(self, direction):
        if direction == 'left':
            self.degrees += self.angle
        elif direction == 'right':
            self.degrees -= self.angle


class Missile(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.velocity = player.velocity * 2
        self.hideturtle()
        self.up()
        self.color('red')
        self.shape('square')
        self.shapesize(0.2, 1.0, None)
        self.showturtle()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.title('Space Station Defence by @wspjoy')
window.bgcolor('black')
window.onkey(window.bye, 'Escape')
window.tracer(0)
window.onclick(lambda x, y: player.get_heading(x, y), btn=1)
window.onkeypress(lambda: player.rotate('left'), 'Left')
window.onkeypress(lambda: player.rotate('right'), 'Right')
window.onkey(lambda: Missile(), 'space')

player_vertices = ((0, 15), (-15, 0), (-18, 5), (-18, -5), (0, 0), (18, -5), (18, 5), (15, 0))
window.register_shape('spaceship', player_vertices)

player = Player()

canvas = window.getcanvas()
print(canvas)
window.listen()

while True:
    window.update()
    player.check_border()
    player.setheading(player.degrees)
    player.forward(player.velocity)
