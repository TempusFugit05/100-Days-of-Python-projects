import tkinter

# Idk how to do it in a better way, but this generates a list of all the acceptable characters for the user input
acceptable_chars = [str(n) for n in range(0, 10)]
acceptable_chars.append(".")

# This defines whether the conversion will be from miles to km or vise versa
switch_state = False
DEFAULT_FONT = "Aharoni"
# A mile is 1.61 kms


window = tkinter.Tk()
window.title("The Epic Converter Project!")
window.minsize(height=500, width=500)
window.config(padx=20, pady=20)

user_input = tkinter.Entry(font=DEFAULT_FONT)
user_input.grid(row=2, column=2)


def convert_mile_to_km(distance):
    """Converts miles to km"""
    distance = round(distance*1.61, 2)
    return distance


def convert_km_to_mile(distance):
    """Converts km to miles"""
    distance = round(distance/1.61, 2)
    return distance


def update_distance(distance):
    global switch_state

    if not switch_state:
        output_message.config(text=str(distance)+" Km")

    else:
        output_message.config(text=str(distance)+" Miles")


def conversion_switcher():
    """Switches between switch states"""
    global switch_state

    if switch_state:
        switch.config(text="Convert From Miles To Km")
        conversion_state.config(text="Km To Miles")
        switch_state = False

    else:
        conversion_state.config(text="Miles To Km")
        switch.config(text="Convert From Km To Miles")
        switch_state = True


def input_validator(user_input, acceptable_chars):
    """Checks if the user input is a valid number"""
    # Return false when string is empty
    if len(user_input) == 0:
        return False
    # This variable checks if the user has put in too many decimal points to prevent errors
    index_points = 0
    # Iterates over all the characters in the user input
    for char in user_input:

        # If a character is not acceptable or is a decimal point in position 0, return False
        if char not in acceptable_chars or (char == "." and user_input.index(char) == 0):
            return False

        # Add 1 to decimal tracker
        elif char == ".":
            index_points += 1

            # Return False if there are more than one decimal point or if the point is in the very end
            if index_points > 1 or (char == "." and user_input.index(char) == len(user_input)-1):
                return False
    # Return True if input passed all checks
    return True


def conversion_handler():
    global acceptable_chars
    global switch_state

    # Gets input string
    raw_input = user_input.get().strip()

    # Proceed if input is valid
    if input_validator(user_input=raw_input, acceptable_chars=acceptable_chars):

        # Convert distance string into a float
        distance = float(raw_input)

        # Calls conversion function based on selected state
        if switch_state:
            update_distance(convert_km_to_mile(distance))

        else:
            update_distance(convert_mile_to_km(distance))

    else:
        output_message.config(text="Invalid input, please try again")


input_button = tkinter.Button(text="Get Answer", font=(DEFAULT_FONT, 10), command=conversion_handler)
input_button.grid(row=1, column=2)

switch = tkinter.Button(text="Convert From Miles To Km", font=(DEFAULT_FONT, 10), command=conversion_switcher)
switch.grid(row=4, column=2)

output_message = tkinter.Label(font=(DEFAULT_FONT, 15))
output_message.grid(row=5, column=2)

conversion_state = tkinter.Label(text="Miles To Km", font=(DEFAULT_FONT, 10))
conversion_state.grid(row=2, column=3)

window.mainloop()