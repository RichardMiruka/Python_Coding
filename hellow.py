# ask user for their name and print a greeting message

name = input ("What is your name? ") # ask the user for their name using the input() function
name = name.strip()                  # remove the space before and after the name using the strip() method
name = name.capitalize()             # capitalize the first letter of the name using the capitalize() method
print(f"Hello, {name}!")             # print the greeting message with the user's name

# name = name.strip().title()   # combine the strip() and title() methods to remove leading and trailing spaces and capitalize the first letter of each word

# The best way to write the code 
# name = input("Enter your name: ").strip().title()
# print(f"Hello, {name}!")
