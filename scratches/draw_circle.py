import turtle as t
from random import randint

t.colormode(255)

screen = t.Screen()


phill = t.Turtle()
phill.speed('fastest')

def random_rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color


screen.bgcolor(random_rgb())

def draw_spiralgraph(size):
    for i in range(int(360 / size)):
        phill.setheading(phill.heading() + 5)
        phill.color(random_rgb())
        phill.circle(100)

draw_spiralgraph(5)


screen.exitonclick()