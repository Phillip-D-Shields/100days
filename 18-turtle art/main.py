from data import rgb_list, better_rgb_list
import turtle as t
import random

t.colormode(255)
t.screensize(500, 500)

dot = t.Turtle()
dot.hideturtle()
dot.penup()
dot.speed('fastest')

screen = t.Screen()
screen.bgcolor(random.choice(better_rgb_list))

dot.setheading(220)
dot.forward(450)
dot.setheading(0)

number_of_dots = 101

for i in range(1, number_of_dots):
    dot.dot(45, random.choice(better_rgb_list))
    # dot.penup()
    dot.forward(75)

    if i % 10 == 0:
        dot.setheading(90)
        dot.forward(65)
        dot.setheading(180)
        dot.forward(750)
        dot.setheading(0)





screen.exitonclick()



