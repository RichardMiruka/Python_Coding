# The code below uses a series of if-elif-else statements to
# compare the value of the variable name against different patterns.

name = input("What is your name? ") # Prompt the user to input their name
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

# reduce reduncancy in the code above  using the following code 
name = input ("what is your name? ")
if name =="Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Unknown")


# The match statement is used to compare the value of house against different patterns
# and execute the corresponding block of code based on the matching pattern.
# In this example, the value "house" is matched against different house names
# from the Harry Potter series, and the corresponding house name is printed to the console. 
# If the value does not match any of the specified patterns, the default case (_) is executed,
# printing "Unknown" to the console.

name = input ("What is your name? ")
match name:
    case "Harry":
        print ("Gryffindor")
    case "Hermione":
        print ("Gryffindor")
    case "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print ("Unknown")

# we can iprove the code above by combining the cases that have the same output into a
# single case statement and using the case keyword to assign the house name to the variable house.
# This reduces redundancy in the code and makes it more concise.

name = input ("What is your name? ")
match name:
    case "Harry", "Hermione", "Ron" => house
    case "Draco" => house
    case _ => house = "Unknown"
print (house)
