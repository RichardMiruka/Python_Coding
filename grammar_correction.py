# Grammar correction using Python                 # Brief description of the script’s purpose

# pip install textblob                            # Instruction to install the required library TextBlob for grammar correction

from textblob import TextBlob                     # Import TextBlob class from the textblob library

def correct_grammar(text):                        # Define a function named correct_grammar that takes in a text argument
    blob = TextBlob(text)                         # Create a TextBlob object using the input text, which enables text processing
    corrected_text = str(blob.correct())          # Use TextBlob's correct() method to suggest grammar/spelling corrections
    return corrected_text                         # Return the corrected text as a string
                                                  
if __name__ == "__main__":                        # Run only if this file is being executed directly as a script
    text = input("Enter your sentence: ")         # Prompt the user to input a sentence for grammar correction
    corrected_text = correct_grammar(text)        # Call the correct_grammar function and store the corrected text
    print(f"Corrected: {corrected_text}")         # Display the corrected text to the user
