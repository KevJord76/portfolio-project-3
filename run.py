# Hangman game categories
categories = ["Sport","Music","Movies"]

# Display the main menu
print("-" * 49)
print("Welcome to the Guess Famous Person Hangman Game")
print("-" * 49)
print("\nPlease select a Category:")

# Display the hangman game categories
for i in range(len(categories)):
    print(str(i+1)+". ", categories[i])  

# Allow the user to exit the game
print("(99 to exit)\n")

# Get the user's choice
choice = input("Please enter your choice:\n")
