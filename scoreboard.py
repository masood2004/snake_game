from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write("Score: ", align="center", move=False,
                   font=("Consolas", 20, "normal"))

    def increment(self):
        self.score += 1
