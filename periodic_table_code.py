# Python code for periodic table
# pip install periodictable

#Add input validation and error handling for periodic table lookup
# Step 1- Check if atomic number input is within the valid range (1-118)
# Step 2- Add error handling for invalid inputs and out-of-range values
# Step 3- Improve user feedback with descriptive error messages



import periodictable

try:
    Atomic_No = int(input("Enter the atomic number (1-118): "))
    if Atomic_No < 1 or Atomic_No > 118:
        raise ValueError("Invalid atomic number. Please enter a number between 1 and 118.")

    element = periodictable.elements[Atomic_No]
    print('Name: ', element.name)
    print('Symbol: ', element.symbol)
    print('Atomic Mass: ', element.mass)
    print('Atomic Number: ', element.number)
    
except ValueError as e:
    print(e)
except KeyError:
    print("Element not found. Please enter a valid atomic number.")
except Exception as e:
    print("An error occurred:", e)
