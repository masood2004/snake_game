# Import the necessary modules
from turtle import Screen
import time

# Import custom classes for food, scoreboard, and snake
from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Set up the screen properties
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen size
screen.tracer(0)  # Disable automatic screen updates
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the window title

# Initialize the scoreboard, snake, and food objects
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Listen for key presses to control the snake
screen.listen()
screen.onkey(snake.up, "Up")  # Move the snake up
screen.onkey(snake.down, "Down")  # Move the snake down
screen.onkey(snake.left, "Left")  # Move the snake left
screen.onkey(snake.right, "Right")  # Move the snake right

# Variable to control the game loop
is_game_on = True

# Start the game loop
while is_game_on:
    screen.update()  # Update the screen after each move
    time.sleep(0.1)  # Pause for a short time to control the speed of the game
    snake.move()  # Move the snake forward

    # Check if the snake collides with the food
    # If the snake's head is close enough to the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random position
        snake.extend()  # Add a new segment to the snake's body
        scoreboard.increment()  # Increase the score

    # Check if the snake hits the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        is_game_on = False  # End the game
        scoreboard.game_over()  # Display the game over message

    # Check if the snake collides with its own body
    for segment in snake.segments[1:]:  # Skip the snake's head
        # If the head collides with any segment
        if snake.head.distance(segment) < 10:
            is_game_on = False  # End the game
            scoreboard.game_over()  # Display the game over message

# Wait for the user to click on the screen to exit the game
screen.exitonclick()
