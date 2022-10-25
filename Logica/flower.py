from turtle import Turtle, Screen

def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

my_radius = int(input("Введите радиус? "))
my_petals = int(input("Сколько листьев вы хотите нарисовать? "))

bob = Turtle()
bob.speed(2)
for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)

bob.hideturtle()

screen = Screen()
screen.exitonclick()

