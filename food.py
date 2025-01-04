# Import the necessary module from the turtle library
from turtle import Turtle
import random  # For generating random positions

# Define the Food class to manage the food object in the game


class Food(Turtle):
    def __init__(self):
        """
        Initialize the food object, setting its shape, color, and size.
        Then, call the refresh method to place the food at a random location.
        """
        super().__init__()  # Call the parent class constructor (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen so it doesn't leave a trail
        # Resize the shape (smaller circle)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the turtle's drawing speed to the fastest
        self.refresh()  # Place the food at a random position on the screen

    def refresh(self):
        """
        Generate a new random position for the food on the screen, ensuring 
        the position is a multiple of 20 (for grid alignment).
        """
        random_x = random.randrange(
            # Random x-coordinate between -280 and 280 (multiple of 20)
            -280, 280, 20)
        # Random y-coordinate between -280 and 280 (multiple of 20)
        random_y = random.randrange(-280, 280, 20)
        # Move the food to the new random position
        self.goto(random_x, random_y)
