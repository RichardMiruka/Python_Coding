# Convert RGB to Hex using Python - Converting a color name to its Hex code using Python

# pip install webcolors - Import the name_to_hex function from the webcolors library

from webcolors import name_to_hex

def color_name_to_code(color_name):                # Define a function to convert a color name to a Hex code
    try:                                           # Use a try-except block to handle exceptions
        color_code = name_to_hex(color_name)       # Convert the color name to a Hex code
        return color_code                          # Return the Hex code
    except ValueError:                             # If the color name is invalid
        return None                                # Return None if the color name is invalid

color_name = input("Enter a color name: ")         #  Get a color name as input from the user
result_code = color_name_to_code(color_name)       # Convert the color name to a Hex code
if result_code:                                    # If the result code is not None
    print(f"Hex code: {result_code}")              # Print the Hex code
else:                                              # If the result code is None
    print("Invalid color name.")                   # Print an error message
