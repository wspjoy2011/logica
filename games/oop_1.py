from turtle import *


class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.velocity = 0.01
        self.up()

    def move(self):
        pass


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.color('white')
        self.velocity = 0
        self.angle = 1
        self.shape('spaceship')

    def increase_velocity(self):
        if self.velocity <= 0.03:
            self.velocity += 0.01

    def move(self, direction):
        if direction == 'up':
            self.increase_velocity()
        elif direction == 'left':
            self.left(self.angle)
        elif direction == 'right':
            self.right(self.angle)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.bgcolor('black')
window.title('Space station defence by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')

window.tracer(0)

spaceship=((0, 15), (-15, 0), (-18, 5), (-18, -5), (0, 0), (18, -5), (18, 5), (15, 0))
window.register_shape('spaceship', spaceship)

player = Player()

window.onkey(lambda: player.move('up'), 'Up')
window.onkeypress(lambda: player.move('left'), 'Left')
window.onkeypress(lambda: player.move('right'), 'Right')
window.listen()

while True:
    window.update()
    player.forward(player.velocity)