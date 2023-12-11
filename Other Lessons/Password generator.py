# Ask how many letters to add to password
# Ask how many symbols
# Ask how many numbers
# combine them and output password
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
choices = [0, 1, 2]

# 0 - letters
# 1 - symbols
# 2 - numbers

password = ""
length = nr_numbers + nr_symbols + nr_letters
for index in range(0, length):
    chosen_character = choices[random.randint(0, len(choices)-1)]
    if chosen_character == 0 and nr_letters != 0:
        password += letters[random.randint(0, len(letters)-1)]
        nr_letters -= 1
    elif chosen_character == 1 and nr_symbols != 0:
        password += symbols[random.randint(0, len(symbols)-1)]
        nr_symbols -= 1
    elif chosen_character == 2 and nr_numbers != 0:
        password += numbers[random.randint(0, len(numbers)-1)]
        nr_numbers -= 1
    if nr_letters == 0 and 0 in choices:
        choices.remove(0)
    elif nr_symbols == 0 and 1 in choices:
        choices.remove(1)
    elif nr_numbers == 0 and 2 in choices:
        choices.remove(2)

print(password)

#lengh -> length
#(select a variable and press shift + f6 to change every instance)

#delete unneeded  spaces