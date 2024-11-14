# variables inside a different scope are not accessible from outside the scope
# In this program, we define a function named get_guess that prompts the user for a guess and returns the input.
# We also define a main function that calls the get_guess function and prints the user's guess.
# Finally, we call the main function to run the program.
# This program demonstrates the use of functions to encapsulate code and improve code organization.
# The get_guess function handles the input logic, while the main function orchestrates the program flow.
# By using functions, we can separate concerns and make the code more modular and easier to understand.
# This program also illustrates the concept of scope, where variables defined inside a function are local to that function.
# The guess variable defined inside the get_guess function is not accessible outside that function's scope.
# This encapsulation helps prevent naming conflicts and makes it easier to reason about the code.
# The main function can safely use the guess variable without worrying about other parts of the program modifying it.
# This separation of concerns and scoping rules are fundamental concepts in programming that help create maintainable code.


def get_guess():                         # Define a function named get_guess
    guess = input("Enter your guess: ")  # Prompt the user for a guess
    return guess                         # Return the user's guess or input

def main():                              # Define a function named main
    guess = get_guess()                  # Call the get_guess function and store the result in the guess variable
    print(f"Your guess is: {guess}")     # Print the user's guess
main()                                   # Call the main function to run the program
