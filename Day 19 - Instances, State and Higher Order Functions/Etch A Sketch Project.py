from turtle import Screen, Turtle

cursor = Turtle()
screen = Screen()


def forward():
    """Move turtle forward"""
    cursor.forward(10)


def back():
    """Move turtle back"""
    cursor.back(10)


def clockwise():
    """Turn turtle clockwise"""
    cursor.left(10)


def counter_clockwise():
    """Turn turtle counter - clockwise"""
    cursor.right(10)


def clear():
    """Clears screen"""
    cursor.clear()

screen.listen()
screen.onkey(fun=back, key="a")
screen.onkey(fun=forward, key="d")
screen.onkey(fun=clockwise, key="w")
screen.onkey(fun=counter_clockwise, key="s")
screen.onkey(fun=clear, key="c")




screen.exitonclick()