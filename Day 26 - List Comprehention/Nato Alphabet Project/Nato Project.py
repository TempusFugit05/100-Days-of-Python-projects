import pandas

# Read the csv file
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create new dictionary and take every row and assign the letter as the key and code as the value
alphabet_extract = {row.letter: row.code for (index, row) in alphabet.iterrows()}

# Or in other words:
# for (index, row) in alphabet.iterrows():
#     print(row.letter)

def create_nato_string():
    # Take user input
    # ADDENDUM: I added a way to catch errors when user enters invalid inputs
    try:
        user_input = input("Word: ").upper()

        # Convert string into list of characters
        char_list = [char for char in user_input]

        # Create list containing the codes for each character in the input
        code_list = [alphabet_extract[char] for char in char_list]

    # Try again if the user inputted an invalid string
    except KeyError:
        print("Please enter a valid string.")
        create_nato_string()

    else:
        print(code_list)

create_nato_string()