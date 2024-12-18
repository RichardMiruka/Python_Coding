# Python program to check email accounts across services

# pip install holehe

import subprocess


def check_email(email):
    """Check if an email account exists."""
    result = subprocess.run(["holehe", email], capture_output=True, text=True)
    return result.stdout


email = input("Enter an email address: ")
result = check_email(email)
print(result)
