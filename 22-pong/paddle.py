from turtle import Turtle

WIDTH_STRETCH = 5
LENGTH_STRETCH = 1


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_STRETCH, stretch_len=LENGTH_STRETCH)
        self.penup()
        self.goto(x, y)

        self.color("white")

    def move_up(self):
        """move the paddle up"""
        if self.ycor() < 240:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def move_down(self):
        """move the paddle down"""
        if self.ycor() > -240:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)


