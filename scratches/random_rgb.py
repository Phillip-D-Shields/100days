import turtle as t
from random import randint



dash = t.Turtle()
t.colormode(255)

def random_rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color



dash.color(random_rgb())

screen = t.Screen()
screen.bgcolor("gray")



screen.exitonclick()



