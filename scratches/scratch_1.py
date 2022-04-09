from turtle import Turtle, Screen
import heroes

timmy = Turtle()

timmy.shape("triangle")
timmy.color("cadet blue")


for _ in range(4):
    timmy.left(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()