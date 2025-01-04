# Import the necessary module from the turtle library
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"  # Text alignment at the center
FONT = ("Consolas", 20, "normal")  # Font style, size, and type

# Define the Scoreboard class to handle score display and updates


class Scoreboard(Turtle):
    def __init__(self):
        """
        Initialize the scoreboard with an initial score of 0, hide the turtle,
        set the text color to white, and place the scoreboard at the top of the screen.
        """
        super().__init__()  # Call the parent class constructor (Turtle)
        self.score = 0  # Initialize the score to 0
        self.hideturtle()  # Hide the turtle cursor (we just need the text)
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top of the screen
        self.color("white")  # Set the text color to white
        self.update_score()  # Display the initial score

    def update_score(self):
        """
        Updates the score on the screen by clearing the previous score and 
        writing the current score in the center at the top of the screen.
        """
        self.clear()  # Clears the previous score displayed
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)  # Display the current score

    def game_over(self):
        """
        Displays the 'GAME OVER' message in the center of the screen.
        """
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER.", align=ALIGNMENT,
                   font=FONT)  # Display the 'GAME OVER' message

    def increment(self):
        """
        Increments the score by 1 and updates the score display.
        """
        self.score += 1  # Increase the score by 1
        self.update_score()  # Update the score on the screen
