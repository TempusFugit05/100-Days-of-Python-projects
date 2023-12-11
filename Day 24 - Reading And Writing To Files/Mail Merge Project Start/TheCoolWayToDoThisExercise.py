#TODO: Create a letter using starting_letter.txt 
#for: each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Read the names list
with open("./Input/Names/invited_names.txt") as names_file:

    # Define variables
    name = ""
    names = []

    # Check if a character is a new line character
    for char in names_file.read():

        # Build name string until end of line
        if char != "\n":
            name += char

        # Reset add name to list and reset name
        else:
            names.append(name)
            name = ""

# Read the template mail
with open("./Input/Letters/starting_letter.txt") as starting_letter_file:

    # Convert email contents into list
    input_email = []
    for char in starting_letter_file.read():
        input_email.append(char)

    for char in input_email:

        # Find start of text to replace
        if char == "[":

            # Save index of start
            start_index = input_email.index(char)

            # Delete character until finding the end
            while char != "]":
                char = input_email[start_index]
                del input_email[start_index]

for name in names:

    # Define variables
    output_email = ""
    template_email = input_email.copy()

    # Create/write to output files
    with open(f"./output/readytosend/for {name}", "w") as output_file:

        # Insert name in designated space
        template_email.insert(start_index, name)

        # Build final email
        for char in template_email:
            output_email += char

        # Write to file
        output_file.write(output_email)

