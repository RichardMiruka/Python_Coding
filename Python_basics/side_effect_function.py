def greet(input):                         # Define a function named greet that takes an input parameter
    if input == "Alice":                  # Check if the input is "Alice"
        return "Hello, Alice!"            # Return "Hello, Alice!" if the input is "Alice"
    else:                                 # If the input is not "Alice"
        return "Hello, stranger!"         # Return "Hello, stranger!" as a default message

print(greet("Bob"))                     # Call the greet function with "Alice" as the input and print the result

