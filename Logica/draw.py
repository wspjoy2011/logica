from turtle import *

SCREEN_SIZE = 800


def draw(x, y):
    pen.ondrag(None)
    pen.setheading(pen.towards(x, y))
    pen.goto(x, y)
    for _ in range(4):
        pen.forward(20)
        pen.left(90)
    pen.ondrag(draw)


def change_color():
    user_color = window.textinput('Color', 'Enter a color: ')
    if user_color:
        pen.color(user_color)


def change_width():
    user_width = window.textinput('Width', 'Enter a width: ')
    if user_width:
        pen.width(int(user_width))


def goto_zero_coord(x, y):
    pen.up()
    pen.goto(0, 0)
    pen.pendown()


def rotate_turtle(x, y):
    pen_x = pen.xcor()
    pen_y = pen.ycor()
    if pen_x -20 <= x <= pen_x + 20 and pen_y - 20 <= y <= pen_y + 20:
        for i in range(0, 360, 6):
            pen.setheading(i)


window = Screen()
window.title('Draw by @wspjoy')
window.setup(SCREEN_SIZE, SCREEN_SIZE)
window.onclick(rotate_turtle, btn=1)
window.onkey(exit, 'Escape')
window.onkey(change_color, 'F1')
window.onkey(change_width, 'F2')



pen = Pen()
pen.shape('turtle')
pen.shapesize(2, 2)
pen.speed(0)
pen.ondrag(draw)
pen.onrelease(goto_zero_coord)

user_color = window.textinput('Color', 'Enter a color: ')
if user_color:
    pen.color(user_color)

user_width = window.textinput('Width', 'Enter a width: ')
if user_width:
    pen.width(int(user_width))

window.listen()
window.mainloop()
