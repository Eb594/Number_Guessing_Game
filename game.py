import random

secret_number = random.randint(1, 100)

while True:
    try:
        guess = float(input("Guess the number (1 or greater): "))

        if guess < 1:
            print("Please enter a number greater than or equal to 1.")
            continue

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if guess == secret_number:
        print("Correct! You won!")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
