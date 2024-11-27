# Python Program to check if a frequency is audio or radio


def check_frequency(frequency):
    """
    Determines whether a given frequency falls within the audio or radio
    frequency range.

    Args:
        frequency (float): The frequency in Hertz (Hz).

    Returns:
        str: A message indicating the type of frequency or if it's invalid.
    """
    if 20 <= frequency <= 20000:
        return "Audio Frequency"
    elif 20000 < frequency <= 200000:
        return "Radio Frequency"
    else:
        return "Invalid Frequency - Neither Audio nor Radio"


def main():
    """
    Main function to get user input and check the frequency type.
    """
    try:
        # Input frequency from the user
        frequency = float(input("Enter the frequency in Hz: "))

        # Check the frequency type and display the result
        result = check_frequency(frequency)
        print(result)

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


# Run the program
if __name__ == "__main__":
    main()
