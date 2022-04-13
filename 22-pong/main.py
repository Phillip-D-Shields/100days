from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("darkgreen")
screen.setup(width=800, height=600)
screen.tracer(0)



l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_is_running = True
while game_is_running:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Check for a collision with the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # make it bounce
        ball.bounce_y()

    # Check for a collision with either paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when the ball hits the left
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect when the ball hits the right
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
