from turtle import Turtle, Screen
from segment import Segment
import time

# Every snake segment is 20 by 20 pixels
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.listen()
screen.tracer(0)

# Create first segment
segments = [[Segment(), 0, 0]]
segments[0][0].create()


def create_segment():
    """Creates new segment at the end of the snake"""
    global segments

    # Creates new segment that inherits the coordinates of the last segment
    segments.append([Segment(), segments[len(segments)-1][1], segments[len(segments)-1][2]])

    # Initializes segment
    segments[len(segments)-1][0].create()

    # Move segment to position
    segments[len(segments)-1][0].move(segments[len(segments)-2][1], segments[len(segments)-2][2])


# Functions that return pressed key
def key_press_w():
    global current_key
    current_key = "w"
def key_press_a():
    global current_key
    current_key = "a"
def key_press_s():
    global current_key
    current_key = "s"
def key_press_d():
    global current_key
    current_key = "d"


# Key logger
screen.onkey(fun=key_press_w, key="w")
screen.onkey(fun=key_press_a, key="a")
screen.onkey(fun=key_press_s, key="s")
screen.onkey(fun=key_press_d, key="d")
screen.onkey(fun=create_segment, key="c")

current_key = "w"

while True:

    # Update screen
    screen.update()

    # Iterate set position for each segment to the one after it, not including the head
    for current_segment in segments:
        segment_index = 1
        if segment_index == 0:
            pass
        else:
            segments[segment_index][1] = segments[segment_index-1][1]
            print(segments[segment_index][1])
            segments[segment_index][2] = segments[segment_index-1][2]
            print(segments[segment_index][2])
            segments[segment_index][0].move(x=segments[segment_index-1][1], y=segments[segment_index-1][2])
        segment_index += 1
        print(segment_index)

    # Move up by one pixel
    if current_key == "w":
        segments[0][2] += 20
        segments[0][0].move(x=segments[0][1], y=segments[0][2])

    # Move left by one pixel
    elif current_key == "a":
        segments[0][1] -= 20
        segments[0][0].move(x=segments[0][1], y=segments[0][2])

    # Move down by one pixel
    elif current_key == "s":
        segments[0][2] -= 20
        segments[0][0].move(x=segments[0][1], y=segments[0][2])

    # Move right by one pixel
    else:
        segments[0][1] += 20
        segments[0][0].move(x=segments[0][1], y=segments[0][2])

    time.sleep(0.2)
