# In this program, we define a function named get_guess that prompts the user for a guess and returns the input.
# We also define a main function that calls the get_guess function and prints the user's guess.
# Finally, we call the main function to run the program.
def get_guess():  # Define a function named get_guess
    guess = int(
        input("Enter your guess: ")
    )  # Prompt the user for a guess and convert the input to an integer
    return guess  # Return the user's guess as an integer


def main():  # Define another function named main that orchestrates the program flow
    guess = get_guess()  # assign the return value of get_guess to the variable guess
    if guess == 50:  # Check if the user's guess is correct
        print(
            "You guessed correctly!"
        )  # Print a success message if the guess is correct
    else:  # If the guess is incorrect
        print("Try again!")  # Print a message to try again


main()
