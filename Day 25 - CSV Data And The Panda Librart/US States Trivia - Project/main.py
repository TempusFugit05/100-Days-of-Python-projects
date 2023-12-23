from turtle import Turtle, Screen
import pandas
from text_drawer import TextDrawer

screen = Screen()
screen.bgpic("blank_states_img.gif")
drawer = TextDrawer()

# Read data
data = pandas.read_csv("50_states.csv")

# Convert state names to list
state_names = list(data["state"])

score = 0

correct_states = []


def input_state():
    """Gets user input"""
    global score

    # Create prompt
    chosen_state = screen.textinput(prompt="Guess a state", title=f"{score}/50").title()

    # Return value from check condition
    return check_input(chosen_state)


def check_input(chosen_state):
    """Checks if state is inside the states list"""
    global score

    # Checks if state was already guessed
    if chosen_state in correct_states:
        print(f"{chosen_state} is already in the list")

    # Checks if state is valid
    elif chosen_state in state_names:

        # Writes state name
        add_to_screen(chosen_state)

        # Adds score
        score += 1

        # Add state to list
        correct_states.append(chosen_state)

        # Return false for end game condition
        return False

    elif chosen_state == "Exit":
        # Returns True for end game condition
        return True

    else:
        print(f"{chosen_state} is a state")


def add_to_screen(chosen_state):
    """Adds state text to screen"""

    # Defining the specific row
    chosen_state = data[data.state == chosen_state].values.tolist()

    # Extract relevant data
    state_name = chosen_state[0][0]
    state_x = chosen_state[0][1]
    state_y = chosen_state[0][2]

    # Write text in correct position
    drawer.write(text=state_name, x=state_x, y=state_y)


def generate_states_to_learn():
    
    # Creating list containing the states that were not guessed this game
    states_to_learn_list = [state for state in state_names
                            if state not in correct_states]

    # Generate states to learn dictionary
    states_to_learn = {
        "State": states_to_learn_list
    }

    # Generate csv file
    states_to_learn = pandas.DataFrame(states_to_learn)
    states_to_learn.to_csv("States To Learn")


def maingame():
    """Main game loop"""

    # Checks if game should end
    exit_game = False

    # Main game loop, ends when exit game condition is met or when player won
    while not exit_game and score < 50:

        # Takes user input and checks if player chose to quit
        exit_game = input_state()

    generate_states_to_learn()



maingame()