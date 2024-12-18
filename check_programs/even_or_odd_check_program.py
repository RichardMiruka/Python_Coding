def is_even(number):
    """
    Check if a given number is even using recursion.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    if number == 0:
        return True
    elif number == 1:
        return False
    else:
        return is_even(number - 2)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_even(num):
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
