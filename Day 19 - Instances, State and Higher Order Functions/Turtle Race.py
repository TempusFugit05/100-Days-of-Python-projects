import turtle
from turtle import Turtle, Screen
from random import randint

turtle.colormode(255)

screen = Screen()

def create_turtles(number_of_turtles):
    # Creates turtles based on the amount of turtles chosen
    all_turtles = []
    for number_of_turtles in range(number_of_turtles):
        all_turtles.append(Turtle())

    return all_turtles


def finish_line(turtle):
    """Checks if turtle won"""

    if not turtle.xcor() <= 300:
        return True
    else:
        return False


def assign_color():
    """Assigns random rbg values to turtle"""
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b


def progress_turtle(turtle):
    """Move turtle forward and check if it won"""
    # Progress turtle forward by random amount
    turtle.forward(randint(1, 20))

    # Check if turtle won
    is_won = finish_line(turtle)

    # If turtle wins, return turtle name and win condition, else return only win condition
    if is_won:
        return is_won, turtle
    else:
        return is_won


def reset_turtles(turtle, originx, originy):
    """Resets turtle positions"""

    # Set new y coordinates
    originy += 50

    # Stop drawing
    turtle.penup()

    # Move to starting x, y position
    turtle.goto(x=originx, y=originy)

    # Start drawing
    turtle.pendown()

    # Return new x y positions
    return originy


def race():

    # Defining boolean to check if race should finish
    is_race_finished = False

    # Define starting x and y coordinates
    originx = -300
    originy = -300

    # Create turtles
    all_turtles = create_turtles(int(screen.numinput(title="Choose number of turtles", prompt="Choose number of turtles", minval=1, maxval=15)))

    # Move turtles to starting position and set new x y coordinates and assign colors
    for i in range(0, len(all_turtles)):

        originy = reset_turtles(turtle=all_turtles[i], originx=originx, originy=originy)

        all_turtles[i].color(assign_color())

    # Progresses each turtle forward while until finish line
    while not is_race_finished:

        # Check for every turtle
        for i in range(0, len(all_turtles)):

            # Fetch turtle from list
            is_race_finished = progress_turtle(all_turtles[i])

            # Stop if turtle won
            if is_race_finished:
                break

    # Display winner
    all_turtles[i].write(arg="I WON!!!", move=False, align="center")


race()
screen.exitonclick()

