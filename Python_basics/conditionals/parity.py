# x = int(input("What is the value of x?"))
# if x % 2 == 0:
#    print("x is even")
# else:
#     print("x is odd")

def main():                                         # Main function that drives the program.
    x = int(input("What is the value of x?"))       # Prompt the user to input an integer value for x
    if is_even(x):                                  # Check if the number is even using the is_even function
        print("x is even")                          # If is_even returns True, x is even
    else:                                           # If is_even returns False, x is odd
        print("x is odd")                           # Print "x is odd" to the console
                                  
# def is_even(n):                                     # Function to determine if a number is even or odd
#    if n % 2 == 0:                                 # Check if n is divisible by 2 (no remainder means it's even)
#       return True                                # Return True if n is even
#   else:
#       return False                               # Return False if n is odd

def is_even(n):                                     # Function to determine if a number is even or odd
    return n % 2 == 0                               # Return True if n is even, False if n is odd

main()                                             # Call the main function to run the program                               
