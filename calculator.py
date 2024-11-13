"""
x = 1
y = 2

z = x + y
print(z) # Output: 3
"""

x = input ("What is X? ")
y = input ("What is Y? ")

# z = x + y      # Output: 12
z = int(x) + int(y)
print(z)

# best way to write the code is to convert the input to an integer directly (nesting the int() function inside the input() function)
# x = int(input("What is X? "))
# y = int(input("What is Y? "))
# print(x + y) # Output: 3

