# Grammar correction using python

# pip install textblob

from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

# Run only if this file is being executed directly as a script
if __name__ == "__main__":
    text = input("Enter your sentence: ")
    corrected_text = correct_grammar(text)
    print(f"Corrected: {corrected_text}")
