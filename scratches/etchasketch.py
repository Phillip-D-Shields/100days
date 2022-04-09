from turtle import Turtle, Screen

phill = Turtle()
screen = Screen()


def move_forward():
    phill.forward(10)


def move_backward():
    phill.backward(10)


def turn_left():
    phill.left(22.5)


def turn_right():
    phill.right(22.5)


def clear_screen():
    screen.reset()


screen.listen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()