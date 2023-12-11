import math
import turtle
from random import randint
"""
It's possible to import a module as a different name
For example:
import turtle as Leonardo
We can now refer to the turtle library as Leonardo
"""

leonardo = turtle.Turtle()
leonardo.hideturtle()
turtle.colormode(255)
leonardo.speed(1000)
leonardo.pensize(3)
New_Screen = turtle.Screen()

# def draw_square():
#     # Challenge 1 - draw a square
#     for i in range(4):
#         print("lol")
#         leonardo.forward(100)
#         leonardo.left(90)
#
#
# draw_square()


# def draw_dotted_line():
#     # Challenge 2 - draw a dotted line
#     for i in range(10):
#         leonardo.forward(10)
#         leonardo.penup()
#         leonardo.forward(10)
#         leonardo.pendown()
#
# draw_dotted_line()


# def draw_shapes():
#     # Draw regular shapes and change their color
#
#     for i in range(3, 100):
#         times_turned = 0
#         # Define/reset total turned degrees
#
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         # Creating random RGB values
#
#         degrees = int(360/i)
#         # Degrees in an angle in a regular polygon
#         leonardo.fillcolor((r, g, b))
#         # Assigning color to fill shape
#
#         leonardo.begin_fill()
#
#         while times_turned < i:
#             # Draw sides while not back to starting position
#
#             leonardo.right(degrees)
#             # Make angle
#
#             leonardo.forward(100)
#             # Side length
#
#             times_turned += 1
#             # Equation for Regular polygon angles
#         leonardo.end_fill()
#
#
#
# draw_shapes()


def generate_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    # Creating random RGB
    return r, g, b

# def random_walk():
#     # Make the turtle turn a random direction and change color to random color
#
#     while True:
#         leonardo.color(generate_random_color())
#         # Assign random color to turtle
#
#         direction = randint(0, 1)
#         # Choose direction
#
#         if direction == 0:
#             leonardo.right(90)
#
#         else:
#             leonardo.left(90)
#
#         leonardo.forward(10)
#
#
# random_walk()

def make_spirograph(definition):
    for i in range(1, definition+1):
        leonardo.color(generate_random_color())
        leonardo.right(360/definition)
        leonardo.circle(100)


make_spirograph(400)
New_Screen.exitonclick()
