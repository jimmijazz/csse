#string of current positions of players
player_positions = str()

def make_initial_state(number_of_players):
        player_positions = str()
	"""Takes number of supporters for each team and gives back the initial state. int -> dictionary"""
	for x in range(number_of_players):
		player_positions += 'T'
		player_positions += 'A'
	player_positions += '__'
	print(player_positions)
	
	
	
