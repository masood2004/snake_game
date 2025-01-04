from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        """Updates the score on the screen."""
        self.clear()  # Clears previous text
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT,
                   font=FONT)

    def increment(self):
        """Increment the score and update the display."""
        self.score += 1
        self.update_score()  # Update score display after increment
