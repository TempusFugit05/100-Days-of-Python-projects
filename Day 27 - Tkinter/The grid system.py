import tkinter

# The grid system allows to easily place widgets in a grid system that makes it easier to position them

# Creating window
window = tkinter.Tk()
window.minsize(height=500, width=500)

# We can add padding around the edges of the screen in order to make things more readable
window.config(padx=25, pady=25)

# Setting first widget in position 0,0
label = tkinter.Label(text="Trololo", font=("Aharoni", 20))
label.grid(row=0, column=0)

# We can also add padding to individual widgets
label.config(padx=50)

# This widget will be on the far right
button1 = tkinter.Button(text="I am a button lol")
button1.grid(row=0, column=3)

# This one will be in between them
button2 = tkinter.Button(text="I am a button 2!")
button2.grid(row=0, column=2)

window.mainloop()