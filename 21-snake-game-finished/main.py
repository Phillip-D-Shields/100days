from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard


# Create a 600 x 600 screen with bg color and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("phills snake game")
screen.tracer(0)


# create snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# screen listen for key press
screen.listen()
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")


game_is_live = True
while game_is_live:
    screen.update()
    time.sleep(0.25)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        print("nom nom")
        snake.extend()
        scoreboard.update_score(1)
        food.refresh()

    # detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.game_over()
        game_is_live = False

    #detect collision with self
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_live = False















screen.exitonclick()