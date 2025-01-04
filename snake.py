# Import the necessary module from the turtle library
from turtle import Turtle

# Constants for the starting position of the snake, movement distance, and directions
# The initial positions of the snake's segments
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15  # How far the snake moves in each step
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHT = 0  # Angle for moving right

# Define the Snake class to create and manage the snake


class Snake():
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
        Create the snake by adding segments to it using the starting positions.
        """
        for position in STARTING_POSITION:  # For each position in the starting position list
            self.add_segment(position)  # Add a segment at that position

    def add_segment(self, position):
        """
        Add a single segment to the snake at the specified position.
        """
        segment = Turtle("square")  # Create a new square-shaped turtle segment
        segment.penup()  # Lift the pen so it doesn't draw while moving
        segment.color("white")  # Set the color of the segment to white
        segment.goto(position)  # Move the segment to the specified position
        # Add the segment to the snake's list of segments
        self.segments.append(segment)

    def extend(self):
        """
        Add a new segment to the snake, extending it.
        This segment is added at the position of the last segment in the snake.
        """
        self.add_segment(
            # Add a segment at the last segment's position
            self.segments[-1].position())

    def move(self):
        """
        Move the snake forward by shifting all segments except the head.
        The head moves forward in the specified direction.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment
            # Get the coordinates of the segment in front of it
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Move the current segment to the position of the segment in front
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head forward by the specified move distance
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Change the direction of the snake to up (90 degrees), 
        unless it's already moving down (270 degrees).
        """
        if self.segments[0].heading() != DOWN:  # Don't allow the snake to move directly down
            self.segments[0].setheading(UP)  # Set the heading to up

    def down(self):
        """
        Change the direction of the snake to down (270 degrees), 
        unless it's already moving up (90 degrees).
        """
        if self.segments[0].heading() != UP:  # Don't allow the snake to move directly up
            self.segments[0].setheading(DOWN)  # Set the heading to down

    def left(self):
        """
        Change the direction of the snake to left (180 degrees),
        unless it's already moving right (0 degrees).
        """
        if self.segments[0].heading() != RIGHT:  # Don't allow the snake to move directly right
            self.segments[0].setheading(LEFT)  # Set the heading to left

    def right(self):
        """
        Change the direction of the snake to right (0 degrees),
        unless it's already moving left (180 degrees).
        """
        if self.segments[0].heading() != LEFT:  # Don't allow the snake to move directly left
            self.segments[0].setheading(RIGHT)  # Set the heading to right
