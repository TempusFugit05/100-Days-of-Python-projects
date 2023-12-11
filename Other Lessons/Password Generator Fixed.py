# Ask how many letters to add to password
# Ask how many symbols
# Ask how many numbers
# combine them and output password
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []


def add_chars(n, char_list, password):
    for i in range(1, n+1):
        password += char_list[random.randint(0, len(char_list)-1)]
    return password


password += add_chars(n=nr_numbers, char_list=numbers, password=password)
password += add_chars(n=nr_symbols, char_list=symbols, password=password)
password += add_chars(n=nr_letters, char_list=letters, password=password)
random.shuffle(password)
password = "".join(password)
print(password)

#lengh -> length
#(select a variable and press shift + f6 to change every instance)

#delete unneeded  spaces