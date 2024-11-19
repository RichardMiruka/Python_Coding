# URL shortener using Python - Tinyurl

# pip install pyshorteners - Import the pyshorteners library

import pyshorteners

long_url = input("Enter the URL to shorten: ")                  # Get the long URL from the user input 
short_url = pyshorteners.Shortener().tinyurl.short(long_url)    # Shorten the URL using the tinyurl service from pyshorteners library 
print("Shortened URL:", short_url)                              # Display the shortened URL to the user 
