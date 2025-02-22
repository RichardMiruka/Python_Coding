import os
import glob

def process_text_files():
    """
    Reads each text file in the current directory, extracts numbers,
    sorts them in ascending order, calculates their sum, and writes the 
    results to a new file with 'processed' in its name.
    
    Each output file will have the following format:
    
    Sorted Numbers:
    <number1>
    <number2>
    ...
    
    Sum: <total_sum>
    """
    # Find all .txt files in the current directory.
    text_files = glob.glob("*.txt")
    
    for filename in text_files:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        numbers = []
        # Process each line in the file
        for line in lines:
            line = line.strip()
            try:
                # Attempt to convert the line to a float
                number = float(line)
                numbers.append(number)
            except ValueError:
                # Ignore lines that cannot be converted to a number
                continue
        
        # Sort numbers in ascending order
        sorted_numbers = sorted(numbers)
        total_sum = sum(sorted_numbers)
        
        # Create a new filename with 'processed' in its name.
        new_filename = f"processed_{filename}"
        with open(new_filename, 'w') as outfile:
            outfile.write("Sorted Numbers:\n")
            for number in sorted_numbers:
                outfile.write(f"{number}\n")
            outfile.write(f"\nSum: {total_sum}\n")
        
        print(f"Processed file '{filename}' and created '{new_filename}'.")

if __name__ == "__main__":
    process_text_files()
