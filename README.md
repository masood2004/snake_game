# Snake Game

Welcome to the Snake Game! This is a Python implementation of the classic Snake Game using the Turtle graphics library. The game allows you to control a snake that grows as it eats food, and the goal is to avoid colliding with walls or the snake's own body.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Game Logic](#game-logic)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/masood2004/snake_game.git
   cd snake-game
   ```

2. **Install dependencies**:
   The game uses the `turtle` module, which comes pre-installed with Python, so there is no need to install any additional libraries if you have Python set up.

3. **Run the game**:
   Execute the following command in your terminal to start the game:
   ```bash
   python main.py
   ```

## How to Play

- Use the arrow keys on your keyboard to control the snake.
  - **Up arrow**: Move the snake up.
  - **Down arrow**: Move the snake down.
  - **Left arrow**: Move the snake left.
  - **Right arrow**: Move the snake right.
  
- The snake grows in size each time it eats the food, and you earn points.
- Avoid hitting the walls or the snake's body. If you collide, the game is over, and your score is displayed on the screen.
  
## Features

- **Score Tracking**: Your current score is displayed at the top of the screen, and it updates each time you eat food.
- **Random Food Placement**: Food appears at random locations on the screen for the snake to eat.
- **Game Over Screen**: If the snake collides with the walls or its own body, the game ends, and a "Game Over" message is displayed.

## Game Logic

1. **Snake Movement**: The snake consists of segments, and the head of the snake controls its movement. Each time the snake moves, the segments follow the head.
2. **Food Interaction**: The food is randomly placed on the screen. If the snake's head touches the food, the snake grows by one segment, and the score increases.
3. **Game Over**: The game ends if the snake hits the wall or collides with its own body.

## Code Structure

### main.py
- This is the main file that runs the game. It initializes the screen, the snake, the food, and the scoreboard. It also contains the game loop where the snake moves and checks for collisions.

### snake.py
- This file contains the `Snake` class that defines the snake's behavior, including movement, growing, and changing direction.

### food.py
- The `Food` class is responsible for generating food at random locations on the screen.

### scoreboard.py
- The `Scoreboard` class handles displaying the score and the game-over message.

## Contributing

Contributions are welcome! If you have suggestions for improving the game, feel free to fork the repository, make changes, and submit a pull request.

Here are a few ways you can contribute:
- Suggest new features or improvements.
- Report bugs or issues.
- Help with documentation.

Please make sure to follow the coding conventions and test your changes before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
