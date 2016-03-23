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

#### TO DO ###

# - Add function to check if user input is not _A or A_

######QUESTIONS DELETE! ! ! ######

# - Is commenting style ok? what is most recommended?
# - Do we get more marks the more efficient/pythonic we are?
# - Should if print the initial state and then call show_current_states(states) or just do show_current_states(states)
# - What happens if user selects one blank and one string should I be using tuples instead?
# - Do we include a 'win function' when number of differences == 0

# - what happens when you get to this state TTAATTA__A

## Discussions ##

#- considered using replace
###########################
def interact():

    
    states = [] # Records history of supporters position
  
    while True:  # Get user input an makes sure it's an int
        number_of_players = (input("How many supporters from each team"))
        if number_of_players.isdigit():
            break
        else:
            print('Please enter an integer')

    # Make initial state and print
    states.append(make_initial_state(number_of_players))
    
    print(states[-1])

    while True:
        blanks = position_of_blanks(states[-1])
        show_current_states(states)
        user_guess=(input("? "))
        
        if user_guess == 'q': # Quit program
            break

        elif user_guess == 'b': # Go back
            if len(states) > 1:
                states.pop()
                show_current_states(states)
            else:
                print('This is the first state')

        # If not 'q' or 'b', make sure input is an integer
        elif not user_guess.isdigit():
            print("Please enter an integer")

        elif int(user_guess) == blanks:
            print("Please select a supporters position")

        elif int(user_guess) > len(states[-1]):
            print("Please enter a number between 0 and " + str(len(states[-1])))

        # Check if position is not _A, A_ or _
        elif int(user_guess) == ((blanks)+1) or int(user_guess) == ((blanks)-1):
            print("Please enter the position of the first blank")

        else:
            make_move(states[-1],user_guess)
            states.append(make_move(states[-1],user_guess))

            
            
def make_initial_state(number_of_players):
    """Takes number of supporters for each team and gives back the initial state.

    int(number of supporters) -> str(first state of supporter positions)"""
    player_positions = str()    # String of current positions of players

    for x in range(int(number_of_players)):
    	player_positions += 'T'
    	player_positions += 'A'

    player_positions += '__'
    return(player_positions)



def make_position_string(length):
    """Takes length of the state and returns a string of numbers representing positions.

    int(number of players) -> str(position of players)"""

    length_string = ""

    count = 0
    for a in range(length):
        if count < 9:
            length_string += str(count)
            count += 1
        else:
            length_string += str(count)
            count = 0
    return(length_string)



def num_diffs(state):
    """Takes current state and returns current number of differences between
    adjacent entries.

    str(supporter positions) -> int(number of differences) """

    number_of_differences = 0

    # If letter != next letter, increment counter
    for n in range(len(state)-1):
        if state[n] != state[n+1]:
            number_of_differences += 1
    return(number_of_differences)



def position_of_blanks(state):
    """Return location of first blank entry in state

    str(supporter positions) -> int(position of blanks)"""

    current_position = 0

    for n in state:
        if n == "_":
            return(current_position)
            break
        else:
            current_position += 1



def make_move(state, position):
    """Return new state where pair at given position has been swapped with blanks.
    Depends on position_of_blanks function.

    str(supporter positions), int(position to move) -> str(updated supporter positions)"""

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

    return(updated_state)



def show_current_states(states):
    """Prints the most current state and:
    - make_position_string
    - state
    - num_diffs
    - position_of_blanks

    list(supporter positions history) -> str,str,int,int"""

    current_state = states[-1]

    print(make_position_string(len(current_state)))
    print((current_state),(num_diffs(current_state)),(position_of_blanks(current_state)))

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
  
