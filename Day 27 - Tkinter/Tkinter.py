# Tkinter is a simple-to-use GUI library
import tkinter

# Defining the tkinter window object
window = tkinter.Tk()

#--------------------------------------------------------------------------------------------------------------
# Defining label object which is just a text displayed in the window
# We can also specify the size and font of the text
label = tkinter.Label(text="testing testing 123", font=("Aharoni", 20))

# It's also possible to later change the attributes of the label object like so:
label["text"] = "This is a proper test."

# Or alternatively:
label.config(text="THIS IS THE FINAL TEST")

# Displays the label and defines how it will be displayed
label.pack(side="left")
#--------------------------------------------------------------------------------------------------------------
# Setting the title of the window
window.title()

# Setting the minimum size the window can be resized to
window.minsize(width=500, height=500)
#--------------------------------------------------------------------------------------------------------------
def button_detector():
    label.config(text="I got clicked!")
    # The place method allows for precise placement of widgets on the screen
    # Alternatively, we could use the grid system
    label.place(x=0, y=0)
# We can also set a function to be triggered when the button is pressed
# In this case the function will simply change the text displayed
button = tkinter.Button(text="This is a button", command=button_detector)

button.pack()
#--------------------------------------------------------------------------------------------------------------
# Tkinter also allows for a user text input

# Setting up the input object and setting its width
user_input = tkinter.Entry(width=5)
user_input.pack()

# Defining the label
custom_label = tkinter.Label()
custom_label.pack()


# Defining the function to be called when the button is pressed
def set_text():
    """This function changes the text displayed in the label to be the text inputted by the user"""
    custom_label.config(text=user_input.get())


# Defining the button
label_change_trigger = tkinter.Button(text="Click me to change the text", command=set_text)
label_change_trigger.pack()
#--------------------------------------------------------------------------------------------------------------
# This function keeps the window open and should be placed at the very end of the code
window.mainloop()
#--------------------------------------------------------------------------------------------------------------