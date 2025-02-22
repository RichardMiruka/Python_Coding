import random

def number_guessing_game():
    """
    Plays a number guessing game.

    The computer randomly selects a number between 1 and 100. The player
    is given seven chances to guess the number. After each guess, the game
    provides feedback on whether the guess is too low or too high.

    Returns:
        None
    """
    secret_number = random.randint(1, 100)
    attempts_allowed = 7

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts_allowed} attempts to guess the number.\n")

    for attempt in range(1, attempts_allowed + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
            continue

        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.\n")
            break
    else:
        # This block executes if the loop completes without a correct guess.
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.\n")

if __name__ == "__main__":
    number_guessing_game()
