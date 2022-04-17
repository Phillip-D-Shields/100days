import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#113f36")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
# screen.onkey(player.move_down, "Down")
# screen.onkey(player.move_left, "Left")
# screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create new car every 0.1 seconds
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

    # detect if player reaches top of screen
    if player.is_at_finish_line():
        scoreboard.update_score()
        player.start_new_round()
        car_manager.level_up()

screen.exitonclick()
