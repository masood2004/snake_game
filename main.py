from turtle import Turtle, Screen
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
