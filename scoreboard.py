# Import the necessary module from the turtle library
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"  # Text alignment at the center of the screen
# Font style, size, and type for the text display
FONT = ("Consolas", 20, "normal")

# Define the Scoreboard class to handle score display and updates


class Scoreboard(Turtle):
    def __init__(self):
        """
        Initialize the scoreboard. Set the initial score to 0, load the high score
        from a file, hide the turtle, and position the scoreboard at the top of the screen.
        """
        super().__init__()  # Call the parent class (Turtle) constructor
        self.score = 0  # Initialize the current score to 0

        # Load the high score from a file (data.txt)
        with open("data.txt") as data:
            # Read and store the high score as an integer
            self.high_score = int(data.read())

        self.hideturtle()  # Hide the turtle cursor (used for graphics, not needed for text)
        self.penup()  # Lift the pen to prevent drawing lines
        # Position the scoreboard at the top center of the screen
        self.goto(0, 270)
        self.color("white")  # Set the text color to white
        self.update_score()  # Display the initial score and high score

    def update_score(self):
        """
        Updates the score on the screen. Clears the previous score and writes the
        current score and high score at the top center of the screen.
        """
        self.clear()  # Clear the previous text from the screen
        # Write the current score and high score on the screen
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Resets the score. If the current score exceeds the high score, updates the high
        score and saves it to a file (data.txt). Resets the current score to 0 and updates
        the scoreboard display.
        """
        # Update high score if the current score exceeds it
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score
            # Save the new high score to the file
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0  # Reset the current score to 0
        self.update_score()  # Update the scoreboard display

    def increment(self):
        """
        Increments the current score by 1 and updates the scoreboard display.
        """
        self.score += 1  # Increase the current score by 1
        self.update_score()  # Update the scoreboard display
