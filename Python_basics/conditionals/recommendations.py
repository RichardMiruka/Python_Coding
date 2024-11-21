def main():
    """
    Main function to gather user preferences and recommend a game based on input.
    """
    difficulty = input("Do you prefer 'Difficult' or 'Casual' games? ").strip().capitalize() # Ask the user for their preferred difficulty level
    players = input("Do you prefer 'Singleplayer' or 'Multiplayer'? ").strip().capitalize()  # Ask the user for their preferred type of gameplay
    
    # Validate inputs and provide game recommendations based on user preferences
    if difficulty == "Difficult" and players == "Singleplayer":
        recommend("Dark Souls")
    elif difficulty == "Difficult" and players == "Multiplayer":
        recommend("Counter-Strike: Global Offensive")
    elif difficulty == "Casual" and players == "Singleplayer":
        recommend("Stardew Valley")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Animal Crossing: New Horizons")
    else:
        print("Sorry, we couldn't find a match for your preferences. Try again!")            #  Default message for unrecognized input

def recommend(game):
    """
    Function to suggest a game based on the user's preferences.
    """
    print(f"You might enjoy playing {game}!")

if __name__ == "__main__":
    main()
