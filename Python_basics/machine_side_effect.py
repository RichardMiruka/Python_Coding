# Define an initial emoticon variable to use in responses
emoticon = "V.V"                          # Corrected emoticon to a valid expression
def main():                               # Define the main function
    global emoticon                       # Declare emoticon as global to modify it within the function
    say("Is anyone there?")               # Call say() function with a greeting phrase
    emoticon = "^.^"                      # Update emoticon to a friendly expression
    say("Oh, hi!")                        # Call say() again with a different phrase

def say(phrase):                          # Define the say function to display phrases with emoticons
    print(phrase + " " + emoticon)        # Corrected syntax to concatenate the phrase with emoticon

main()                                    # Call the main function to execute the script
