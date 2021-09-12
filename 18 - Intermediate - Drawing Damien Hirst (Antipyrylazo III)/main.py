import colorgram
import turtle as t
import random as r

sonic = t.Turtle()
t.colormode(255)
sonic.shape("turtle")
sonic.penup()
sonic.speed(0)


colors = colorgram.extract('image.jpg', 50)
color_list = []

for color in colors:
    color_list.append(tuple(color.rgb))

pos_x = -250
pos_y = -250

for i in range(20):
    sonic.goto(pos_x, pos_y)
    for _ in range(10):
        sonic.dot(20, r.choice(color_list))
        sonic.forward(50)
    pos_y += 30

screen = t.Screen()
screen.exitonclick()
