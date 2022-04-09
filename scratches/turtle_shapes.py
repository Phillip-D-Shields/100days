from turtle import Turtle, Screen
from random import randint
from data import colors


dash = Turtle()
dash.shape('turtle')
dash.color('coral')

dot = Turtle()
dot.shape('circle')
dot.color('green')

screen = Screen()
screen.bgcolor("gray")

# dashed line
# for _ in range(10):
#     dash.forward(10)
#     dash.penup()
#     dash.forward(10)
#     dash.pendown()
#
#


def draw_square(turtle, length):
    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)


def draw_triangle(turtle, length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)


def draw_pentagon(turtle, length):
    for _ in range(5):
        turtle.forward(length)
        turtle.left(72)


def draw_hexagon(turtle, length):
    for _ in range(6):
        turtle.forward(length)
        turtle.left(60)


def draw_heptagon(turtle, length):
    for _ in range(7):
        turtle.forward(length)
        turtle.left(51.42)


def draw_octagon(turtle, length):
    for _ in range(8):
        turtle.forward(length)
        turtle.left(45)


def turtle_draw(turtle, length):
    draw_triangle(turtle, length)
    draw_square(turtle, length)
    draw_pentagon(turtle, length)
    draw_hexagon(turtle, length)
    draw_heptagon(turtle, length)
    draw_octagon(turtle, length)


# turtle_draw(dash, 125)


def draw_shape(number_of_sides, turtle, length):
    color = colors[randint(0, len(colors) - 1)]
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        turtle.color(color)
        turtle.forward(length)
        turtle.right(angle)



for i in range(3, 11):
    draw_shape(i, dot, 125)

screen.exitonclick()



