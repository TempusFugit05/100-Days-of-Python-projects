from turtle import Turtle, Screen
# The turtle library is used to draw simple graphics and comes preinstalled with pycharm
# Importing turtle and screen classes

turtle = Turtle()
# Accessing the turtle class inside the turtle library and assigning it to a new variable

print(turtle)
# In this case, the physical location of the turtle object in the memory will be printed

turtle.shape("turtle")
# Assigning turtle shape tp the turtle by accessing the turtle method

turtle.color("green")
# Assigning color green to the turtle through the color method

screen = Screen()
# Assigning screen class to new variable

turtle.forward(100)
# Moving turtle by 100 by accessing the forward method

print(screen.canvheight)
# Accessing screen height attribute
# An attribute is a variable associated with a class

screen.exitonclick()
# Calling the screen exit on click method
# A method is a function associated with a class

