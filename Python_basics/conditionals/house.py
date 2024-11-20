# The code above uses a series of if-elif-else statements to
#  compare the value of the variable name against different patterns.
name = input("What is your name?")  # Prompt the user to input their name
if name == "Harry":                 # Check if the name is "Harry"
    print("Gryffindor")             # If the name is "Harry", print "Gryffindor"
elif name == "Hermione":            # Check if the name is "Hermione"
    print("Gryffindor")             # If the name is "Hermione", print "Gryffindor"
elif name == "Ron":                 # Check if the name is "Ron"
    print("Gryffindor")             # If the name is "Ron", print "Gryffindor"
elif name == "Draco":               # Check if the name is "Draco"
    print("Slytherin")              # If the name is "Draco", print "Slytherin"
else:                               # If the name does not match any of the above conditions
    print("Unknown")                # Print "Unknown"



# and execute the corresponding block of code based on the matching pattern.
# In this example, the value "house" is matched against different house names
# from the Harry Potter series, and the corresponding house name is printed to the console. 
# If the value does not match any of the specified patterns, the default case (_) is executed,
# printing "Unknown" to the console.

# using the match statement to compare the value of house against different patterns
match house:
    case "Gryffindor":
        print("Gryffindor")
    case "Hufflepuff":
        print("Hufflepuff")
    case "Ravenclaw":
        print("Ravenclaw")
    case "Slytherin":
        print("Slytherin")
    case _:
        print("Unknown")
# The match statement is 