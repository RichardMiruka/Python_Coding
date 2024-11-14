def greet(text):                          # Add 'text' as a parameter to the function
    if "hello" in text.lower():           # Check if "hello" (case-insensitive) is in the text
        return "Hello, there"             # Return a greeting if "hello" is in text
    else:
        return "I am not sure what you mean" # Default response if "hello" isn't in text

greeting = greet("hello, Richard")        # Call the function with the input string
print(greeting + ", Richard")             # Concatenate the greeting with "Richard"

