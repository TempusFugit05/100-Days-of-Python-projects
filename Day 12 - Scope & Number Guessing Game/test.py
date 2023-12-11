import random
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Used later to check if user input is a number


def maingame():
    """Main game loop. Handles everything :)"""
    choose_difficulty = input("Choose difficulty: Easy or Hard\n").lower()
    # Choosing a difficulty

    while choose_difficulty != "easy" and choose_difficulty != "hard":
        print("Error")
        choose_difficulty = input("Choose difficulty: Easy or Hard\n").lower()
        # A while loop handle player not entering correct difficulty

    print(f"You chose to play {choose_difficulty.title()} mode")

    if choose_difficulty == "easy":
        lives = 10
    else:
        lives = 5
    # Assigns lives based on chosen difficulty

    number = random.randint(1, 100)
    # Chooses a number to guess

    guess = ""
    # Defines guess variable to be used in the while loop

    while guess != number and lives > 0:
        # Main game loop. Breaks when player wins or loses

        guess = input(f"You have {lives} lives left\nPick a number between 1 - 100\n")
        # User input

        is_valid_number = True
        while is_valid_number:
            for character in guess:
                if character not in number_list:
                    is_valid_number = False
                #Checks if user input is a valid number.

            if guess == "":
                is_valid_number = False
                # Invalidates empty input

            if is_valid_number:
                break
                # Breaks loop if a valid number was entered

            else:
                guess = input(f"Not a valid number\nPlease enter a valid number\n")
                # Else, enter a new number

            is_valid_number = True

        guess = int(guess)
        # Converts input to an integer.

        if guess > number:
            print("Number too high")
            lives -= 1
        elif guess < number:
            print("Number too low")
            lives -= 1
        # Prints whether guess is high or low and subtracts a life

    if guess == number:
        play_again = input("You won!\nPlay again?\n").lower()
    else:
        play_again = input("You Lost!\nPlay again?\n").lower()
    # Prints whether player lost or not, and asks to play again

    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
        print("Error")
        play_again = input("Play again?").lower()
    # Detects if player entered wrong answer

    if play_again == "yes" or play_again == "y":
        maingame()
    # Starts new game if answer is positive


maingame()
print("See ya later!")