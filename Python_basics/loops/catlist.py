#!/usr/bin/env python
"""
This script prints 'meow' a user-specified number of times.
It demonstrates the use of a while loop for input validation 
and a for loop for iteration.
"""

while True:
    # Ask the user to input a positive integer
    n = int(input("What is n? "))

    # Break the loop if the input is a positive integer
    if n > 0:
        break

# Loop n times to print "meow"
for i in range(n):
    print("meow")
