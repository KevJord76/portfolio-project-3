# Import the random library
import random

# Import the os library
import os

# Import the time library
import time

# Hangman game categories
categories = ["Sport","Music","Movies","Authors","General Knowledge"]

# Sport dictionary of famous names and clues
sport = {
    'Lionel Messi': 'Argentine football player',
    'Serena Williams': 'American tennis player',
    'LeBron James': 'American basketball player',
    'Lydia Ko': 'New Zealand golfer',
    'Max Verstappen': 'Belgian-Dutch motorsports racing driver'
}

# Music dictionary of famous names and clues
music = {
    'Dermot Kennedy': 'Irish singer-songwriter',
    'Taylor Swift': 'American singer-songwriter',
    'Lewis Capaldi': 'Scottish singer-songwriter',
    'Ellie Goulding': 'English singer-songwriter',
    'Kylie Minogue': 'Australian singer-songwriter'
}

# Movies dictionary of famous names and clues
movies = {
    'Tom Hanks': 'Forrest Gump',
    'Margot Robbie': 'I, Tonya',
    'Kate Winslet': 'Titanic',
    'Leonardo DiCaprio': 'The Wolf of Wall Street',
    'Will Smith': 'Men in Black'
}

# Authors dictionary of famous names and clues
authors = {
    'Stephen King': 'The Shining',
    'J. K. Rowling': 'Harry Potter',
    'John Grisham': 'The Firm',
    'Sally Rooney': 'Normal People',
    'John Irving': 'The Cider House Rules'
}

# General knowledge dictionary of famous names and clues
general = {
    "Seán O'Casey": 'Irish dramatist and memoirist',
    'Joan of Arc': 'Saint',
    'Nelson Mandela': 'South African anti-apartheid activist',
    'Édith Piaf': 'French singer, lyricist and actress',
    'Marie Curie': 'Polish-French physicist',
    'Cristiano Ronaldo': 'Portuguese footballer',
    'Rihanna': 'Barbadian singer',
    'Winston Churchill': 'Former Prime Minister of the United Kingdom',
    'Volodymyr Zelenskyy': 'Ukrainian leader',
    'Constance Markievicz': 'Irish politician, revolutionary, nationalist, suffragist, socialist'
}

def display_menu():
    """
    Display the hangman game main menu
    """
    print("-" * 49)
    print("Welcome to Guess the Famous Person Hangman Game")
    print("-" * 49)
    print("\nPlease select a Category:")

    # Display the hangman game categories
    for i in range(len(categories)):
        # Remember index starts at zero
        print(str(i+1)+". ", categories[i])  

    # Allow the user to exit the game
    print("(99) to exit\n")

def clear_screen():
    """
    Clear the screen
    """
    os.system('clear')
        
def validate_choice(chosen):
    """
    Validate the menu choice made by the user:
    Inside the try, converts chosen string into an integer
    Raises valueError if string cannot be converted into an integer 
    or if the choice is not within the menu parameters or 99
    """
    try:
        chosen = int(chosen)
        # Is the user choice valid? 
        if not chosen in range(1,len(categories)+1) and not chosen == 99:
            raise ValueError("incorrect menu option")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again!\n")  
        # Pause the output to allow the user to see the error message
        time.sleep(2); 
        return False

    return True   

def validate_character(letter):
    """
    Check if the user has entered a value from A-Z or a full-stop or a single quote 
    Also check that only one character has been entered 
    """
    # Is the character valid? 
    valid_letter = (letter.isalpha()) and (len(letter) == 1)

    # Also check for the characters of "." and "'", which a name could contain
    if (letter == ".") or (letter == "'"):
        valid_letter = True
    
    return valid_letter   

def get_random_person(category):
    """
    Convert the chosen category dictionary into a list 
    and randomly select a famous person from the list
    """
    selected_list = list(category.items())
    # Get a random name from the list
    random_person = random.choice(selected_list)
    
    return random_person

def display_life_lines(lives_left):
    """
    Display the number of life lines the user has left
    """
    if lives_left == 1:
        print(f"You have only {lives_left} life line left...\n")
    else:
        print(f"You have {lives_left} life lines left...\n")

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
        # Print underscores and spaces to denote the characters in the name or else print the found characters 
        for char in name:
            if (char != " ") and (char not in right_guesses):
                # Print underscore and space
                print("_", end=' ')
                # Still letter(s) to be found 
                winner = False
            else:
                # Print correct letter and space
                print(char, end=' ')
        print("\n")

        # Has the user won?
        if winner:
            # This game has ended with a win
            print("Congrats! You have won the game!")
            print(f"You have guessed the famous person: {name}")
            break

        # Ask the user for a character
        character = input("Please enter a character:\n")
        # Clear the screen
        clear_screen()
        
        # Is the input valid?
        valid_input = validate_character(character)
        if not valid_input:
            print(f'Please note!\nYou must enter only 1 valid name character, you entered:"{character}"\n')
        else:
            # Valid Input
            character = character.upper()
            # Has this letter been guessed before?
            if (character in right_guesses) or (character in wrong_guesses):
                print(f'Please note!\nYou have already guessed this letter:"{character}", please try again:\n')
            else:
                # Is the character in the name?
                if character in name:
                    print("Well done! This letter is in the famous person's name")
                    right_guesses += character
                    # Display the number of life lines left
                    display_life_lines(life_lines)                    
                else:
                    print("Hard luck, this letter is not in the famous person's name")
                    wrong_guesses += character
                    life_lines -= 1
                    if life_lines == 1:
                        # Display the number of life lines left
                        display_life_lines(life_lines)
                        # Ask the user if they want to see a clue
                        see_clue = input("Do you want to see a clue? Y/y to see one, any key to continue:\n")
                        see_clue = see_clue.upper()
                        # Display a clue for the user
                        if see_clue == "Y":
                            print(f"\n{clue}")
                    elif life_lines == 0:
                        # This game has ended with a loss
                        print("Sorry you are out of life lines! You have lost this game...\n")
                    else:
                        # Display the number of life lines left
                        display_life_lines(life_lines)  
    
def end_game_message():
    """
    Say good bye to the user 
    """
    print("\nBye, bye, please play again soon!")

def main():
    """
    Run main program functions
    """
    
    # Get the user's menu choice
    while True:  
        # Clear the screen
        clear_screen()
        # Display the menu
        display_menu()      
        choice = input("Please enter your choice:\n")
        
        # Is the input valid?
        valid_input = validate_choice(choice)
        if valid_input:
            # Clear the screen
            clear_screen()
            # Convert to an integer
            choice = int(choice)
            # Exit the game
            if choice == 99:
                # Display end of game message
                end_game_message()
                exit() 
            else:
                # Valid menu option chosen
                category = categories[choice-1]
                print(f"You chose option no {choice}. {category}")                                
                # Check which category was chosen
                if choice == 1:
                    name_and_clue = get_random_person(sport)
                elif choice == 2:
                    name_and_clue = get_random_person(music)                    
                elif choice == 3:
                    name_and_clue = get_random_person(movies)
                elif choice == 4:
                    name_and_clue = get_random_person(authors)
                else:
                    name_and_clue = get_random_person(general)

                # We now have a name to play the game
                play_game(name_and_clue)

                # Ask the user if they want to play again
                play_again = input("\nDo you want to play again? N/n to exit, any key to continue:\n")
                play_again = play_again.upper()    
                if play_again == "N":
                    # Display end of game message
                    end_game_message()
                    break 
  
# Call the main function
main()