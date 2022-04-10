from turtle import Turtle, Screen
import time
from snake import Snake

# Create a 600 x 600 screen with bg color and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("phills snake game")
screen.tracer(0)


# create snake
snake = Snake()

screen.listen()
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")


game_is_live = True
while game_is_live:
    screen.update()
    time.sleep(0.5)
    snake.move()

















screen.exitonclick()