# Import the necessary modules
from turtle import Screen
import time

# Import custom classes for food, scoreboard, and snake
# These should be defined in separate files: food.py, scoreboard.py, and snake.py
from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Set up the screen properties
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size to 600x600 pixels
screen.tracer(0)  # Disable automatic screen updates for smoother animation
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the title of the game window

# Initialize the scoreboard, snake, and food objects
# These are instances of the custom classes created
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Configure key bindings to control the snake
screen.listen()  # Enable the screen to listen for keypress events
screen.onkey(snake.up, "Up")  # Bind the "Up" arrow key to move the snake up
# Bind the "Down" arrow key to move the snake down
screen.onkey(snake.down, "Down")
# Bind the "Left" arrow key to move the snake left
screen.onkey(snake.left, "Left")
# Bind the "Right" arrow key to move the snake right
screen.onkey(snake.right, "Right")

# Variable to control the game loop
is_game_on = True

# Start the game loop
while is_game_on:
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.1)  # Pause for a short time to control the game speed
    snake.move()  # Move the snake forward by a set distance

    # Check if the snake collides with the food
    if snake.head.distance(food) < 15:  # If the snake's head is close to the food
        food.refresh()  # Move the food to a new random position
        snake.extend()  # Add a new segment to the snake's body
        scoreboard.increment()  # Increase the score on the scoreboard

    # Check if the snake hits the wall
    if (
        snake.head.xcor() > 295 or snake.head.xcor() < -295 or
        snake.head.ycor() > 295 or snake.head.ycor() < -295
    ):
        scoreboard.reset()  # Reset the score
        snake.reset()  # Reset the snake to its initial state

    # Check if the snake collides with itself
    # Loop through all segments except the head
    for segment in snake.segments[1:]:
        # If the head collides with a segment
        if snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the score
            snake.reset()  # Reset the snake to its initial state

# Wait for the user to click on the screen to close the game window
screen.exitonclick()
