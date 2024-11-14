# Ask user for their name and print a greeting message
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Ask user for their age and print a message based on their age
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
    
# Ask user for a number and print if it is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
