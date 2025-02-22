# Write a program that reads a text file, finds all sentences that contain 
# a given keyword, and saves those sentences in another text file.
# The program should have a GUI that allows the user to select the 
# input file, supply the keyword, and select the output file

import tkinter as tk
from tkinter import filedialog, messagebox
import re

def select_input_file():
    # Open a dialog to select the input file
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        input_file_var.set(filepath)

def select_output_file():
    # Open a dialog to select the output file location
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filepath:
        output_file_var.set(filepath)

def process_file():
    input_path = input_file_var.get()
    output_path = output_file_var.get()
    keyword = keyword_entry.get()

    # Basic error checks for missing input
    if not input_path:
        messagebox.showerror("Error", "Please select an input file.")
        return
    if not output_path:
        messagebox.showerror("Error", "Please select an output file.")
        return
    if not keyword:
        messagebox.showerror("Error", "Please enter a keyword.")
        return

    try:
        # Read the entire content from the input file
        with open(input_path, "r", encoding="utf-8") as infile:
            text = infile.read()

        # Split text into sentences using a regular expression.
        # This pattern looks for punctuation marks followed by one or more spaces.
        sentences = re.split(r'(?<=[.!?]) +', text)

        # Filter sentences that contain the keyword (case-insensitive search)
        filtered_sentences = [s for s in sentences if keyword.lower() in s.lower()]

        # Write the filtered sentences to the output file
        with open(output_path, "w", encoding="utf-8") as outfile:
            for sentence in filtered_sentences:
                outfile.write(sentence.strip() + "\n")

        # Inform the user about the number of sentences found
        messagebox.showinfo("Success", f"Found {len(filtered_sentences)} sentence(s) containing '{keyword}'.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main application window
root = tk.Tk()
root.title("Keyword Sentence Finder")

# Define StringVar variables to hold file paths
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()

# Create a frame for better layout management
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Input file selection row
tk.Label(frame, text="Input File:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, textvariable=input_file_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Keyword entry row
tk.Label(frame, text="Keyword:").grid(row=1, column=0, sticky="w")
keyword_entry = tk.Entry(frame, width=50)
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

# Output file selection row
tk.Label(frame, text="Output File:").grid(row=2, column=0, sticky="w")
tk.Entry(frame, textvariable=output_file_var, width=50).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_output_file).grid(row=2, column=2, padx=5, pady=5)

# Process button to execute the file processing
tk.Button(frame, text="Process", command=process_file).grid(row=3, column=1, pady=10)

# Start the GUI event loop
root.mainloop()
