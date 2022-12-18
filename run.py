import random

# Hangman game categories
categories = ["Sport","Music","Movies"]

# Sport dictionary list of famous names and clues
sport = {
    'Lionel Messi': 'Argentine football player',
    'Serena Williams': 'American tennis player',
    'LeBron James': 'American basketball player',
    'Lydia Ko': 'New Zealand golf player',
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
    Inside the try, converts string into an integer
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
    print(random_sports_person)

def main():
    """
    Run all program functions
    """
    display_menu()

    # Get the user's menu choice
    while True:        
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
                    get_random_sports_person()
                
                    
                break   

        

# Call the main function
main()