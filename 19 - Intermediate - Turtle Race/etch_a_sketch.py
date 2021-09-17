from turtle import Turtle, Screen

sonic = Turtle()
screen = Screen()


def move_forwards():
    sonic.forward(10)


def move_backwards():
    sonic.backward(10)


def move_lef():
    new_heading = sonic.heading() + 10
    sonic.setheading(new_heading)


def move_right():
    new_heading = sonic.heading() - 10
    sonic.setheading(new_heading)


def clean():
    sonic.home()
    sonic.clear()



screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_lef, "a")
screen.onkey(move_right, "d")
screen.onkey(clean, "c")

screen.exitonclick()








