from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.level = 0
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
