from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.bgcolor("black")

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="enter your winner", prompt="enter the color of the turtle you think will win")
print(user_bet)

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-75, -50, -25, 0, 25, 50]
all_turtles = []

for i in range(0, 6):
    new_turdle = Turtle(shape="turtle")
    new_turdle.color(colors[i])
    new_turdle.penup()
    new_turdle.goto(x=-235, y=y_positions[i])
    all_turtles.append(new_turdle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turdle in all_turtles:
        if turdle.xcor() > 230:
            is_race_on = False
            winning_color = turdle.pencolor()
            if winning_color == user_bet:
                print(f"noice, you win. {winning_color} is the winner")
            else:
                print(f"you lose, {winning_color} won")

        random_distance = randint(0, 11)
        turdle.forward(random_distance)

screen.exitonclick()