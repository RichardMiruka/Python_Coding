# Python Program to check if a number is a palindrome

def check_palindrome(number):
    """
    Checks if a given number is a palindrome.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Negative numbers are not considered palindromes.")
        else:
            result = check_palindrome(number)
            print("Is the number a palindrome?", result)

            if result:
                print("The number is a palindrome.")
            else:
                print("The number is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
