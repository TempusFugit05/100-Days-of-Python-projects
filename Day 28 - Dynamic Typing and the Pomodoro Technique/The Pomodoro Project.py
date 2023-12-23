import tkinter
import math

DEFAULT_FONT = "Times"
BACKGROUND_COLOR = "#1BB6A1"
TEXT_COLOR = "#F3FF66"
WORK_TIME = int(25 * 60)
REST_TIME = int(5 * 60)

timer_toggle = True
work_state = False
time_goal = WORK_TIME
current_time = 0
work_mode = True

#--------------------------------------------------------------------------------------------------------------
# Main window
window = tkinter.Tk()
window.minsize(500, 500)
window.config(bg=BACKGROUND_COLOR, pady=50, padx=100)
window.title("The Pomodoro Project")
#--------------------------------------------------------------------------------------------------------------
# Converting image to an object tkinter can work with
image = tkinter.PhotoImage(file="Kitchen_Timer.gif")

# Creating canvas to display image
# * The highlight thickness attribute prevents white edges around the image
logo = tkinter.Canvas(width=250, height=250, bg=BACKGROUND_COLOR, highlightthickness=0)

# Placing image inside canvas
logo.create_image(120, 150, image=image)
logo.grid(row=1, column=1)
#--------------------------------------------------------------------------------------------------------------
# Main title
title = tkinter.Label(text="THE POMODORO PROJECT!", background=BACKGROUND_COLOR,
                      fg=TEXT_COLOR, font=(DEFAULT_FONT, 15, "bold"))

title.grid(row=0, column=1)
#--------------------------------------------------------------------------------------------------------------
# Timer text
timer = tkinter.Label(text="25:00", font=(DEFAULT_FONT, 25, "bold"), background=BACKGROUND_COLOR,
                      fg=TEXT_COLOR)

timer.grid(row=2, column=1)
#--------------------------------------------------------------------------------------------------------------
work_state_label = tkinter.Label(text="WORK!", bg=BACKGROUND_COLOR, fg=TEXT_COLOR,
                                 font=(DEFAULT_FONT, 30, "bold"))
work_state_label.grid(row=3, column=1)
#--------------------------------------------------------------------------------------------------------------


def time_calculator(elapsed_time, goal):
    # Calculate elapsed seconds
    seconds = 60 - elapsed_time % 60

    # Calculate elapsed minutes
    minutes = int(goal/60 - math.floor(elapsed_time/60))

    return minutes, seconds


def time_string_builder(seconds, minutes):
    """Calculates the minutes and seconds and builds a string out of them"""

    # Add a zero if number is single digit
    if seconds < 10:
        seconds = "0" + str(seconds)

    # Add a zero if number is single digit
    if minutes < 10:
        minutes = "0" + str(minutes)

    # Make string to be displayed as elapsed time
    timer_string = f"{str(minutes)}:{str(seconds)}"

    return timer_string


def reset_time():
    global current_time
    current_time = 0


def time_handler(time):
    """Increment time"""
    time += 1
    return time


def work_state_switcher_on():
    """Switches working state to on"""
    global work_state

    if not work_state:
        work_state = True
        main()


def work_state_switcher_off():
    """Switches working state to off"""
    global work_state

    if work_state:
        work_state = False


def work_mode_switch():
    global work_mode
    work_mode = not work_mode


def update_timer(time, goal):
    """Updates the on-screen timer"""

    # Calculate the amount of seconds and minutes that have passed
    minutes, seconds = time_calculator(elapsed_time=current_time, goal=time_goal-1)

    # Change displayed time text by calling string builder function
    timer.config(text=time_string_builder(minutes=minutes, seconds=seconds))


def update_work_mode_text(state):
    """Sets displayed text to correspond to current working state"""

    if state:
        work_state_label.config(text="WORK!")

    else:
        work_state_label.config(text="TAKE A BREAK BUDDY!")


def main():
    global current_time, WORK_TIME, REST_TIME, time_goal, work_mode

    # Increment time and call main function as long as program is not paused
    if work_state:
        window.after(1000, main)
        current_time = time_handler(current_time)

    # If not reached timer end, proceed normally
    if current_time <= time_goal:
        update_timer(time=current_time, goal=time_goal)

    # Else, reset timer and switch allocated time
    else:

        if work_mode:
            time_goal = REST_TIME
            work_mode_switch()

        else:
            time_goal = WORK_TIME
            work_mode_switch()

        # Reset
        reset_time()

        # change the displayed text
        update_work_mode_text(work_mode)


#--------------------------------------------------------------------------------------------------------------
# Button to start timer
start_button = tkinter.Button(text="START", font=(DEFAULT_FONT, 15, "bold"), bg=TEXT_COLOR,
                              command=work_state_switcher_on)

start_button.grid(row=1, column=0)
#--------------------------------------------------------------------------------------------------------------
# Button to stop timer
stop_button = tkinter.Button(text="STOP", font=(DEFAULT_FONT, 15, "bold"), bg=TEXT_COLOR,
                             command=work_state_switcher_off)

stop_button.grid(row=1, column=2)
#--------------------------------------------------------------------------------------------------------------
window.mainloop()