import turtle as t
from random import randint
from data import colors, directions

t.colormode(255)

def random_rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color


dash = t.Turtle()
dash.shape('square')
dash.width(5)


dot = t.Turtle()
dot.shape('circle')
dot.width(10)


screen = t.Screen()
screen.bgcolor("gray")


def random_move(turtle, length):
    random_heading = directions[randint(0, len(directions) - 1)]
    random_color = random_rgb()

    turtle.color(random_color)
    turtle.setheading(random_heading)
    turtle.forward(length)


for i in range(105):
    random_move(dash, 25)
    random_move(dot, 50)

screen.exitonclick()



