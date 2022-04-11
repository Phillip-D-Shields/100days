from turtle import Turtle

ALIGN = "center"
FONT = ("Serif", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_score(0)

    def update_score(self, score):
        self.score += score
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
