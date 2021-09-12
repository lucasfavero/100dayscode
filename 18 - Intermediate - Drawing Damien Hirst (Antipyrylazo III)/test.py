import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.speed(0)
timmy.pensize(3)
turtle.colormode(255)

angles = [90, 180, 270, 360]


# Drawing dotted
def draw_dot(movement):
    for _ in range(movement):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.down()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple([r, g, b])


for i in range(3, 11):
    timmy.pencolor(random_color())
    for _ in range(i):
        draw_dot(5)
        timmy.right(360 / i)
timmy.clear()

for _ in range(200):
    timmy.right(random.choice(angles))
    timmy.pencolor(random_color())
    timmy.forward(30)
timmy.clear()
turtle.goto(0, 0)

for i in range(1, 361):
    timmy.right(i)
    timmy.pencolor(random_color())
    timmy.circle(150)




screen = Screen()
screen.exitonclick()
