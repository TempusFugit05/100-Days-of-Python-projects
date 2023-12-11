# In this project I make a painting in the  style of Damien Hirst

import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.hideturtle()

my_turtle.speed(1)

my_turtle.penup()
my_turtle.setx(-300)
my_turtle.sety(-300)
my_turtle.pendown()
# Set turtle starting position while making sure to not draw a line

turtle.colormode(255)
# Setting turtle color mode to rgb values

screen = turtle.Screen()

screen_size_x = 500
screen_size_y = 500
screen.screensize(screen_size_x, screen_size_y)
# Set screen size


def x_cords(current_x_coords, horizontal_offset):
    """Finds new x coords to draw circle"""

    # Calculates new x coords
    new_x_coords = current_x_coords + horizontal_offset

    return new_x_coords


def y_cords(current_y_coords, vertical_offset):
    """Finds new y coords to draw circle"""
    # Calculates new y coords
    new_x_coords = current_y_coords + vertical_offset

    return new_x_coords


def generate_new_color():
    """Generates random rgb color"""

    # Generate red value
    r = random.randint(0, 255)

    # Generate green value
    g = random.randint(0, 255)

    # Generate blue value
    b = random.randint(0, 255)

    # Return rgb values
    rgb = r, g, b
    return rgb


def draw_circle(x_coords, rgb):
    """Draws circle"""

    # Change turtle color
    my_turtle.color(rgb)

    # Draw circle
    my_turtle.begin_fill()
    my_turtle.circle(10)
    my_turtle.end_fill()

    # Move to new x position
    my_turtle.penup()
    my_turtle.setx(x_coords)
    my_turtle.pendown()


def reset_position(x_origin, y_origin):
    """Reset turtle position to draw new circle line"""

    # Set turtle x coordinates to starting x position
    my_turtle.penup()
    my_turtle.setx(x_origin)
    my_turtle.pendown()

    # Set new y position to start drawing next line of circles
    my_turtle.penup()
    my_turtle.sety(y_origin)
    my_turtle.pendown()


def main(horizontal_circles, vertical_circles):
    """Main function of program"""
    global screen_size_x, screen_size_y

    # Calculating distance to move on each iteration
    horizontal_offset = screen_size_x / vertical_circles
    vertical_offset = screen_size_y / vertical_circles

    # Defining starting x position
    x_origin = -300

    # Defining starting y position
    y_origin = -300

    # Iterates over number of vertical circles
    for n in range(vertical_circles):

        # Iterates for circles in line
        for i in range(horizontal_circles + 1):

            # Draw a circle and move to new position
            draw_circle(x_coords=x_origin, rgb=generate_new_color())

            x_origin = x_cords(current_x_coords=x_origin, horizontal_offset=horizontal_offset)

        # Resetting x coordinates
        x_origin = -300

        # Changing y coordinates
        y_origin += vertical_offset

        # Move to start of line and move up to draw new circle line
        reset_position(x_origin=x_origin, y_origin=y_origin)


main(10, 10)
screen.exitonclick()