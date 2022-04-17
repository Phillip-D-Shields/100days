from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.current_speed = MOVE_DISTANCE
        self.penup()
        self.seth(90)
        self.start_new_round()

    def move_up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    # def move_down(self):
    #     y = self.ycor() - MOVE_DISTANCE
    #     self.goto(self.xcor(), y)
    #
    # def move_left(self):
    #     x = self.xcor() - MOVE_DISTANCE
    #     self.goto(x, self.ycor())
    #
    # def move_right(self):
    #     x = self.xcor() + MOVE_DISTANCE
    #     self.goto(x, self.ycor())

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def start_new_round(self):
        self.goto(STARTING_POSITION)