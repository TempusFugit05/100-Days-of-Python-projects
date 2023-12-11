from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def test():
    """This function is used as an argument for the screen.onkey func"""
    my_turtle.forward(10)


screen.listen()
# Checks for key presses

screen.onkey(fun=test, key="a")
# This is an example of a higher order function where a function is being passed as an argument

screen.exitonclick()