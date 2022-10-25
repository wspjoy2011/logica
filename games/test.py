from turtle import *
from random import randint
from  tkinter import messagebox

def move_turtle(turtle):
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.goto(x + randint(1, 10), y)

border = Turtle()
border.speed(0)
border.hideturtle()
border.up()
border.width(5)
border.goto(300, -100)
border.left(90)
border.down()
border.forward(200)

turtle_red = Turtle()
turtle_red.name = 'red'
turtle_red.speed(0)
turtle_red.hideturtle()
turtle_red.up()
turtle_red.shape('turtle')
turtle_red.color('red')
turtle_red.goto(0, 50)
turtle_red.showturtle()

turtle_blue = Turtle()
turtle_blue.name = 'blue'
turtle_blue.speed(0)
turtle_blue.hideturtle()
turtle_blue.up()
turtle_blue.shape('turtle')
turtle_blue.color('blue')
turtle_blue.goto(0, -50)
turtle_blue.showturtle()

turtles = [turtle_red, turtle_blue]

while True:
    for turtle in turtles:
        x = turtle.xcor()
        if x > 300:
            messagebox.showinfo('Winner', turtle.name)
            exit()
        move_turtle(turtle)


exitonclick()