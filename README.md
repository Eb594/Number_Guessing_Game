# 🎮 Number Guessing Game

## About the Project

The Number Guessing Game is a beginner-friendly Python project that allows a player to guess a randomly generated secret number.

The computer selects a random whole number between 1 and 100. The player enters guesses until they find the correct number.

After each guess, the program tells the player whether the guess is too high or too low.

The game accepts both integers (whole numbers) and floating-point numbers (decimal numbers) greater than or equal to 1.

## Features

- Generates a random secret number between 1 and 100.
- Accepts whole numbers and decimal numbers as guesses.
- Allows guesses greater than 100, although they will be too high.
- Rejects numbers below 1.
- Handles invalid input without crashing.
- Provides feedback when a guess is too high or too low.
- Continues until the player guesses the correct number.

## Technologies Used

- **Python 3**
- Python's built-in `random` module.

No external libraries are required.

## Requirements

To run this project, you need:

- Python 3 installed on your computer.
- A terminal or command-line interface.
- A text editor such as Nano or Visual Studio Code.

## Project Structure

```text
number-guessing-game/
├── game.py
└── README.md
```

## How to Run the Game

### 1. Clone or download the project

If you have downloaded the project, open your terminal and navigate to its folder.

### 2. Check that Python is installed

Run:

```bash
python3 --version
```

### 3. Start the game

Run:

```bash
python3 game.py
```

### 4. Play the game

Enter a number when prompted.

The program will tell you whether your guess is too high, too low, or correct.

Keep guessing until you find the secret number.

## Example Gameplay

```text
Guess the number (1 or greater): 50
Too high!

Guess the number (1 or greater): 25
Too low!

Guess the number (1 or greater): 35
Correct! You won!
```

*Note: The example above assumes the computer selected 35 as the secret number.*

## How the Code Works

### 1. Importing the Random Module

```python
import random
```

This imports Python's built-in `random` module, which provides functions for generating random numbers.

### 2. Generating the Secret Number

```python
secret_number = random.randint(1, 100)
```

This selects a random whole number between 1 and 100, including both endpoints.

The selected number is stored in the `secret_number` variable.

### 3. Repeating the Game

```python
while True:
```

This creates a loop that allows the player to keep guessing until the correct number is entered.

### 4. Receiving the Player's Guess

```python
guess = float(input("Guess the number (1 or greater): "))
```

The `input()` function receives the player's entry as text.

The `float()` function converts that entry into a number that can be a whole number or a decimal.

### 5. Validating the Guess

```python
if guess < 1:
    print("Please enter a number greater than or equal to 1.")
    continue
```

This checks whether the player's guess is less than 1.

If it is, the program displays an error message and asks the player to try again.

### 6. Handling Invalid Input

```python
except ValueError:
    print("Invalid input! Please enter a valid number.")
    continue
```

The `try` and `except` statements handle inputs that cannot be converted into numbers, such as `hello`.

Instead of crashing, the program displays an error message and continues.

### 7. Checking the Guess

```python
if guess == secret_number:
    print("Correct! You won!")
    break
elif guess > secret_number:
    print("Too high!")
else:
    print("Too low!")
```

These conditional statements compare the guess with the secret number.

- `if` checks whether the guess is correct.
- `elif` checks whether the guess is greater than the secret number.
- `else` handles guesses that are lower than the secret number.
- `break` ends the loop when the player wins.

## Important Notes

- The computer generates a whole-number secret between 1 and 100.
- The player can enter whole numbers or decimal numbers.
- Guesses must be greater than or equal to 1.
- There is no upper limit on the player's guess.
- A guess above 100 will always be too high because the secret number cannot exceed 100.
- Decimal guesses are accepted, but the secret number is always a whole number.

## Possible Improvements

The project can be expanded with additional features, such as:

- Counting the number of attempts.
- Allowing the player to choose a difficulty level.
- Giving the player a limited number of guesses.
- Asking whether the player wants to play again.
- Displaying the secret number when the game ends.
- Adding a leaderboard to record high scores.

## Learning Objectives

This project provides practice with fundamental Python concepts:

- Variables and data types.
- User input using `input()`.
- Type conversion using `float()`.
- Conditional statements using `if`, `elif`, and `else`.
- Loops using `while`.
- Loop control using `break` and `continue`.
- Error handling using `try` and `except`.
- Random number generation using `random.randint()`.

## Author

Created as a beginner Python programming project to practise problem-solving and fundamental programming concepts.

## License

This project is available for educational and personal learning purposes.