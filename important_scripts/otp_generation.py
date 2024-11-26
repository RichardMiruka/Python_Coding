"""
This script generates a secure random OTP (One-Time Password)
using Python's `secrets` module.
The `generate_otp` function takes an optional argument `length`
to specify the length of the OTP to generate.
By default, it generates a 6-digit OTP.
The function uses the `secrets.choice` method to randomly select
characters from the string "0123456789" to create the OTP.

"""

import secrets


def generate_otp(length=6):
    """
    Generate a random OTP (One-Time Password) of the specified length.

    Args:
        length (int): The length of the OTP to generate. Default is 6.

    Returns:
        str: The randomly generated OTP.
    """
    # Validate the OTP length
    if length <= 0:
        raise ValueError("OTP length must be greater than 0.")

    # Define the possible characters for the OTP
    characters = "0123456789"

    # Generate a random OTP using the specified length and characters
    otp = "".join(secrets.choice(characters) for _ in range(length))

    return otp


if __name__ == "__main__":
    # Generate and display an OTP
    otp = generate_otp()
    print("Generated OTP:", otp)
