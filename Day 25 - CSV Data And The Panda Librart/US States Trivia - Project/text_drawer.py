from turtle import Turtle


class TextDrawer:
    def __init__(self):
        self.turtle = Turtle()

    def goto(self, x, y):
        """Moves turtle object to new position without drawing"""
        self.turtle.penup()
        self.turtle.goto(x=x, y=y)
        self.turtle.pendown()

    def write(self, text, x, y):
        self.turtle.hideturtle()
        self.goto(x, y)
        self.turtle.write(arg=text, font=("aharoni",10 , "normal"))