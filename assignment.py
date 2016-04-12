#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4261634
#
#   Student Name: Joshua Bitossi
#
###################################################################

def interact():
    """

    interact() -> None
    """
    states = [] # Records history of supporters position
    while True:  # Get user input an makes sure it's an int
        number_of_players = input("How many supporters from each team? ")
        if number_of_players.isdigit():
            break
        else:
            print('Please enter an integer')

    # Make initial state and print
    states.append(make_initial_state(number_of_players))

    while True:
        blanks = position_of_blanks(states[-1])
        show_current_states(states)
        user_guess=(input("? "))
        
        if user_guess == 'q': # Quit program
            break

        elif user_guess == 'b': # Go back
            if len(states) > 1:
                states.pop()
            else:
                print('This is the first state')

        # If not 'q' or 'b', make sure input is an integer
        elif not user_guess.isdigit():
            print("Please enter an integer")

        elif int(user_guess) == blanks:
            print("Please select a supporters position")

        else:
            user_guess = int(user_guess)
            if blanks - 1 <= user_guess <= blanks + 1:
                print("Please enter a valid move")
            elif user_guess > len(states[-1]):
                print("Please enter a number between 0 and ", len(states[-1]))
            else:
                make_move(states[-1],user_guess)
                states.append(make_move(states[-1],user_guess))
            
            
def make_initial_state(number_of_players):
    """Takes number of supporters for each team and gives back the initial state.

    make_initial_state(int) -> str
    """
    player_positions = str()    # String of current positions of players

    for x in range(int(number_of_players)):
    	player_positions += 'T'
    	player_positions += 'A'

    player_positions += '__'
    return player_positions


def make_position_string(length):
    """Takes length of the state and returns a string of numbers representing positions.

    make_position_string(int) -> str
    """

    length_string = ""

    count = 0
    for a in range(length):
        if count < 9:
            length_string += str(count)
            count += 1
        else:
            length_string += str(count)
            count = 0
    return length_string


def num_diffs(state):
    """Takes current state and returns current number of differences between
    adjacent entries.

    num_diffs(str) -> int
    """

    number_of_differences = 0

    # If letter != next letter, increment counter
    for n in range(len(state)-1):
        if state[n] != state[n+1]:
            number_of_differences += 1
    return number_of_differences


def position_of_blanks(state):
    """Return location of first blank entry in state

    position_of_blanks(str) -> int
    """
    current_position = 0

    for n in state:
        if n == "_":
            return current_position
        else:
            current_position += 1


def make_move(state, position):
    """Return new state where pair at given position has been swapped with blanks.
    Depends on position_of_blanks function.

    make_move(str,int) -> str
    """

    updated_state = ""
    position = int(position)
    blanks = position_of_blanks(state)
    moving_team_members = str(state[position]+state[position+1])     # Supporters to be moved

    count = 0
    while count < len(state):
        # If blank spaces at current position of count, replace with moving team members
        if count == blanks:
            updated_state += moving_team_members
            count += 2

        # If count is at user specified position, update with blanks
        elif count == position:
            updated_state += "__"
            count += 2

        else:
            updated_state += state[count]
            count += 1

    return updated_state


def show_current_states(states):
    """Prints the most current state, number of differences and move count:

    show_current_states(list) -> None
    """

    current_state = states[-1]

    print(make_position_string(len(current_state)))
    print((current_state),(num_diffs(current_state)),(len(states)-1))

##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
#
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
   interact()
   
