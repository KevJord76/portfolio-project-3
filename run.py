# Import the random library
import random

# Import os library
import os

# Hangman game categories
categories = ["Sport","Music","Movies"]

# Sport dictionary list of famous names and clues
sport = {
    'Lionel Messi': 'Argentine football player',
    'Serena Williams': 'American tennis player',
    'LeBron James': 'American basketball player',
    'Lydia Ko': 'New Zealand golfer',
    'Max Verstappen': 'Belgian-Dutch motorsports racing driver'
}

def display_menu():
    """
    # Display the hangman game main menu
    """
    print("-" * 49)
    print("Welcome to Guess the Famous Person Hangman Game")
    print("-" * 49)
    print("\nPlease select a Category:")

    # Display the hangman game categories
    for i in range(len(categories)):
        print(str(i+1)+". ", categories[i])  

    # Allow the user to exit the game
    print("(99 to exit)\n")

def validate_choice(chosen):
    """
    Validate the menu choice made by the user:
    Inside the try, converts chosen string into an integer
    Raises valueError if string cannot be converted into an integer 
    or if the choice is not within the menu parameters or 99
    """
    try:
        chosen = int(chosen)
        if not chosen in range(1,len(categories)+1) and not chosen == 99:
            raise ValueError("incorrect menu option")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again!\n")   
        return False

    return True   

def get_random_sports_person():
    """
    Convert the sport dictionary into a list and
    randomly select a sports star from the list
    """
    sport_list = list(sport.items())
    random_sports_person = random.choice(sport_list)
    
    return random_sports_person

def play_game(game_name_and_clue):
    """
    Play the hangman game with the randomly selected famous person 
    """
    
    # Store the name and clue
    name = game_name_and_clue[0].upper()
    clue = game_name_and_clue[1]

    # Store the right and wrong guessed characters
    right_guesses = ""
    wrong_guesses = ""
    
    # This is the number of wrong guesses the user is allowed 
    life_lines = 6

    # Inform the user
    print("\nCan you guess the famous person below?")
    print(f"You have {life_lines} life lines in total\n")

    # As long as the user has life lines left, keep playing
    while life_lines > 0: 
        # If this stays at True the user has won
        winner = True
        # Print underscores and spaces to denote the characters in the name or else print the valid characters 
        for char in name:
            if (char != " ") and (char not in right_guesses):
                print("_", end=' ')
                # Still letter(s) to be found 
                winner = False
            else:
                print(char, end=' ')
        print("\n")

        # Has the user won?
        if winner:
            # This game has ended with a win
            print(f"Congrats! You have won the game! You have guessed the famous person: {name}")
            break

        # Ask the user for a character
        character = input("Please enter a character:\n")
        character = character.upper()
        if (character in right_guesses) or (character in wrong_guesses):
            print(f'You have already guessed this letter:"{character}", please try again:')
        else:
            # Is the character in the name?
            if character in name:
                print("Well done! This letter is in the famous person's name")
                right_guesses += character
            else:
                print("Hard luck, this letter is not in the famous person's name")
                wrong_guesses += character
                life_lines -= 1
                if life_lines == 1:
                    # Ask the user if they want to see a clue
                    print(f"You have only {life_lines} life line left...\n")
                    see_clue = input("Do you want to see a clue? Y/y to see one, any key to continue:\n")
                    see_clue = see_clue.upper()
                    # Display a clue for the user
                    if see_clue == "Y":
                        print(clue)
                elif life_lines == 0:
                    # This game has ended with a loss
                    print("Sorry you are out of life lines! You have lost this game...\n")
                else:
                    print(f"You have {life_lines} life lines left...\n")

        

    
def main():
    """
    Run all program functions
    """
    
    # Get the user's menu choice
    while True:  
        # Clear the screen
        os.system('clear')
        # Display the menu
        display_menu()      
        choice = input("Please enter your choice:\n")
        if validate_choice(choice):
            # Convert to an integer
            choice = int(choice)
            # Exit the game
            if choice == 99:
                print("Bye, bye, please play again soon!")
                exit() 
            else:
                # Valid menu option chosen
                category = categories[choice-1]
                print(f"You chose option no {choice}. {category}")                                
                if choice == 1:
                    name_and_clue = get_random_sports_person()
                
                # We now have a name to play the game, convert the name to uppercase
                play_game(name_and_clue)

                # Ask the user if they want to play again
                play_again = input("\nDo you want to play again? N/n to exit, any key to continue:\n")
                play_again = play_again.upper()    
                if play_again == "N":
                    break   

        

# Call the main function
main()