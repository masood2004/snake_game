# Import the necessary module from the turtle library
from turtle import Turtle

# Constants for the starting position of the snake, movement distance, and directions
# Initial positions of the snake's segments
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15  # How far the snake moves in each step
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHT = 0  # Angle for moving right

# Define the Snake class to create and manage the snake


class Snake:
    def __init__(self):
        """
        Initialize the snake with an empty list of segments and create the snake
        with the starting positions.
        """
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Create the initial snake
        # The head of the snake is the first segment
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the snake by adding segments at the starting positions.
        """
        for position in STARTING_POSITION:  # Loop through each starting position
            self.add_segment(position)  # Add a segment at that position

    def add_segment(self, position):
        """
        Add a single segment to the snake at the specified position.
        """
        segment = Turtle("square")  # Create a new square-shaped turtle segment
        segment.penup()  # Lift the pen to prevent drawing lines
        segment.color("white")  # Set the color of the segment to white
        segment.goto(position)  # Move the segment to the specified position
        # Add the segment to the list of segments
        self.segments.append(segment)

    def reset(self):
        """
        Reset the snake to its initial state. Move all current segments off-screen,
        clear the list of segments, and recreate the snake.
        """
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        # Update the head to the new first segment
        self.head = self.segments[0]

    def extend(self):
        """
        Add a new segment to the snake by appending it at the position of the last segment.
        """
        self.add_segment(
            # Add a segment at the last segment's position
            self.segments[-1].position())

    def move(self):
        """
        Move the snake forward by shifting the positions of all segments except the head.
        The head moves forward by the set distance.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment
            # Get the x-coordinate of the segment in front
            new_x = self.segments[seg_num - 1].xcor()
            # Get the y-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()
            # Move the segment to the new position
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head forward by the specified distance
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Change the direction of the snake to up (90 degrees),
        unless it is already moving down (270 degrees).
        """
        if self.head.heading() != DOWN:  # Prevent reversing direction
            self.head.setheading(UP)  # Set the heading to up

    def down(self):
        """
        Change the direction of the snake to down (270 degrees),
        unless it is already moving up (90 degrees).
        """
        if self.head.heading() != UP:  # Prevent reversing direction
            self.head.setheading(DOWN)  # Set the heading to down

    def left(self):
        """
        Change the direction of the snake to left (180 degrees),
        unless it is already moving right (0 degrees).
        """
        if self.head.heading() != RIGHT:  # Prevent reversing direction
            self.head.setheading(LEFT)  # Set the heading to left

    def right(self):
        """
        Change the direction of the snake to right (0 degrees),
        unless it is already moving left (180 degrees).
        """
        if self.head.heading() != LEFT:  # Prevent reversing direction
            self.head.setheading(RIGHT)  # Set the heading to right
