from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.score()

    def score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
