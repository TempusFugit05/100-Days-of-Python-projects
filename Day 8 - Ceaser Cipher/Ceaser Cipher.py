import string
alphabet = list(string.ascii_lowercase)

def encrypt(shift, word):
    word = word.lower()
    word = list(word)
    # Converting the inputted text into a list
    letter_index = 0
    for letter in word:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
        else:
            print(letter_index)
            word[letter_index] = letter
            letter_index += 1
            shift -= 1
        # Calculating the index of every letter in the given word in the alphabet
        # Tests if the current character is a letter
        shifted_letter_index = letter_index
        for i in range(0, abs(shift)):
            # Iterates for the absolute value of "shift" to work with negative numbers
            shifted_letter_index += int(shift / abs(shift))
            # Divides shift over the absolute number of shift to check if the index should go backwards or forwards
            if shifted_letter_index > len(alphabet)-1 or shifted_letter_index < -len(alphabet)+1:
                shifted_letter_index = 0
                # Checks if the index is out of bounds, if it is, revert back to 0 to loop over the alphabet
        word[word.index(letter)] = alphabet[shifted_letter_index]
    print(''.join(word))


def decrypt(shift, word):
    word = word.lower()
    word = list(word)
    # Converting the inputted text into a list
    letter_index = 0
    for letter in word:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
        else:
            letter_index += 1
        # Calculating the index of every letter in the given word in the alphabet
        for i in range(0, abs(shift)):
            # Iterates for the absolute value of "shift" to work with negative numbers
            letter_index += -int(shift / abs(shift))
            # Divides shift over the absolute number of shift to check if the index should go backwards or forwards
            # Does the opposite of the encrypt function in terms of the letter index
            if letter_index > len(alphabet)-1 or letter_index < -len(alphabet)+1:
                letter_index = 0
                # Checks if the index is out of bounds, if it is, revert back to 0 to loop over the alphabet
        word[word.index(letter)] = alphabet[letter_index]
    print(''.join(word))


def initialize_crypt():
    choice = input("Type 'encrypt' to encrypt and 'decrypt' to decrypt.\n")
    if choice.lower() == "encrypt":
        encrypt(shift=int(input("Choose a shifting number\n")), word=input("What would you like to encrypt?\n"))
    elif choice.lower() == "decrypt":
        decrypt(shift=int(input("Choose a shifting number\n")), word=input("What would you like to encrypt?\n"))
    else:
        print("error")
        initialize_crypt ()


initialize_crypt()