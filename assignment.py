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

    states = []
    #Explain task
    print("----------WELCOME----------\n\n-INSTRUCTIONS-\nTottenham (T) and Arsenal (A) football club supporters are sitting next to each other.\nThere are two blank chairs at the end of the row.\nYour task is to move the supporters until they are all sitting next to supporters of the same team.\n")
    #Keybindings
    print("-KEYS- \nEnter a number to move the supporters at that position to the empty chairs.\nPress 'b' to move back a state\nPress 'q' to quit. \n")

    #check to make sure it is a number
    number_of_players = input("How many supporters are there on each team?")
    states.append(make_initial_state(number_of_players))
    print(states[-1])
    while True:
        blanks = position_of_blanks(states[-1])
        show_current_states(states)
        user_guess=(input("?"))

        #Quit program
        if user_guess == 'q':
            print("Thank you for playing")
            break

        #Show previous state or print statement if first state
        elif user_guess == 'b':
            if len(states) > 1:
                del(states[-1])
                show_current_states(states)
            else:
                print('This is the first state')

        #make sure input is an integer
        elif not user_guess.isdigit():
            print("Please enter an integer")

        elif user_guess == blanks:
            print("Please select a supporters position")

        elif int(user_guess) > len(states[-1]):
            print("Please enter a number between 0 and " + str(len(states[-1])))

        else:
            make_move(states[-1],user_guess)
            states.append(make_move(states[-1],user_guess))


def make_initial_state(number_of_players):
    """Takes number of supporters for each team and gives back the initial state.

    int -> str"""
    player_positions = str()    #string of current positions of players

    for x in range(int(number_of_players)):
    	player_positions += 'T'
    	player_positions += 'A'
    player_positions += '__'
    return(player_positions)


def make_position_string(length):
    """Takes length of the state and returns a string of numbers representing positions.

    int -> str"""

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

    str -> int """

    #Counter for number of differences
    number_of_differences = 0

    #if letter at n does not equal letter at n+1 increment counter
    for n in range(len(state)-1):
        if state[n] != state[n+1]:
            number_of_differences += 1
    return(number_of_differences)


def position_of_blanks(state):
    """Return location of first blank entry in state

    str -> int"""

    #count of current position
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

    str, int -> str"""

    position = int(position)
    #Updated state
    updated_state = ""
    #Get current position of blanks
    blanks = position_of_blanks(state)
    #characters (team members) to be moved
    moving_team_members = str(state[position]+state[position+1])

    count = 0
    while count < len(state):
        #if blank spaces at current position of count, replace with moving team members
        if count == blanks:
            updated_state += moving_team_members
            count += 2

        #if count is at user specified position, update with blanks
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

    list -> str,str,int,int"""

    current_state = states[-1]

    print(make_position_string(len(current_state)))
    print(current_state)
    print(num_diffs(current_state))
    print(position_of_blanks(current_state))

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

	
	
