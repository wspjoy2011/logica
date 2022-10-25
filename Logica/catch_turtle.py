from turtle import *
from random import randint
from time import sleep


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
time_speed = 2


def random_move():
    x = randint(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20)
    y = randint(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2 - 20)
    enemy.goto(x, y)


def catch_enemy(x, y):
    print('test')
    enemy_x = enemy.xcor()
    enemy_y = enemy.ycor()
    if enemy_x - 20 < x < enemy_x + 20 and\
        enemy_y - 20 < y < enemy_y + 20:
        enemy.hideturtle()
        pen = Pen()
        pen.hideturtle()
        pen.write('You win!', font=('Arial', 30, 'bold'), align='center')


window = Screen()
window.title('Catch turtle by @wspjoy')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')
window.onclick(catch_enemy, btn=1)

enemy = Turtle()
enemy.speed(0)
enemy.color('red')
enemy.shape('turtle')
enemy.shapesize(2, 2)
enemy.up()


window.listen()
while True:
    random_move()
    sleep(time_speed)
