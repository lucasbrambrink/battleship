## VIEWS FOR BATTLESHIP GAME ##
from blessings import Terminal

t = Terminal()

## GLOBAL FUNCTIONS
def clear_screen():
	print (t.clear)

def sign_in():
	clear_screen()
	return input("""
		Welcome to Battleship!!

		Who is signing in right now?\n
		""")

def sign_out():
	clear_screen()
	print("""
		Thank you! I hope you had fun!
		""")


## MENU VIEWS

def welcome_back(name):
	clear_screen()
	input("""

		Welcome back """+name+"!!!!!\n")

def initial_visit(name):
	clear_screen()
	input("""

		This must be your first time here, """+name+""".

		But not to worry, it's easy and fun!\n""")

def main_menu():
	clear_screen()
	print("""Main Menu:

		[1] Start a New Game
		[2] Battle the AI!
		[3] View High Scores
		[4] Exit

		""")
	return input("How would you like to proceed?\n")


## IN-GAME VIEWS


def print_both_boards(game_board1,game_board2):
	clear_screen()
	for i in range(0,len(game_board1)):
		left_margin = "        "
		separator = "             |             "
		row = left_margin+"".join(game_board1[i])+t.yellow(separator)+"".join(game_board2[i])
		print(row)

def place_boat(boat_name):
	present = "\n\nYou are placing %s on the board\n" % (boat_name)
	print(present)
	x,y,orientation = 11,11,None
	while x > 10 or x < 1:
		x = input("X Coordinate: ")
		try:
			x = int(x)
		except:
			x = 11
	while y > 10 or y < 1:
		y = input("Y Coordinate: ")
		try:
			y = int(y)
		except:
			y = 11
	while orientation != "left" and orientation != "right" and orientation != "down" and orientation != "up":
		orientation = input("""How would you like to orient the boat?
			choose [left, right, up or down]
			""")
	return x-1,y-1,orientation

def prompt_boat_placement():
	clear_screen()
	response = input("""         Would you like to place your boats yourself,\n         or have them randomly placed on the board for you?

		[1] Place them myself
		[2] Place them for me

		[3] Exit\n""")
	if response == "1" or response.lower() == "myself" or response.lower() == "me" or response.lower() == "place them myself":
		return 1
	elif response == "2" or response.lower() == "random" or response.lower() == "for me" or response.lower() == "place them for me":
		return 2
	elif response == "3" or response.lower() == "exit":
		quit()
	else:
		prompt_boat_placement()

def ask_boat(array):
	print("\nYour Arsenal:\n")
	for item in array:
		print("    >>>   "+item[:-1]),
	print("\n    >>>   exit")
	while True:
		boat = input("\n\nPlease choose a boat to place:\n")
		for item in array:
			if boat == item[:-1]:
				return boat
			if boat == 'exit':
				quit()
		print("Invalid boat!")

def not_water():
	input("There is something in the way!")

def outside_scope():
	input("The boat would fall off the board!")



def placed_all_boats():
	return input("""
		Success! You were able to place all your boats.
		Get ready to fire some shots!!
		""")

def take_shot():
	print("Now take a shot at your opponent!")
	x,y = 11,11
	while x > 10 or x < 1:
		x = input("X Coordinate: ")
		if x == "exit":
			return "exit","exit"
		try:
			x = int(x)
		except:
			x = 11
	while y > 10 or y < 1:
		y = input("Y Coordinate: ")
		if x == "exit":
			return "exit","exit"
		try:
			y = int(y)
		except:
			y = 11
	return x-1,y-1

def hit_ship(name):
	input("Your "+name+" has been hit!!")

def sunk_ship(name):
	input("The computer sunk your "+name+"!!!")

def sunk_opponent_ship(name):
	input("You sunk the computer's "+name+"!!!!")

def question_to_save():
	clear_screen()
	return input("""
		Would you like to save the game?\n""")

def end_game_win():
	clear_screen()
	input("""

		Congratulations! You beat the powerful AI!

		His ships have been vanquished!""")

def end_game_loss():
	clear_screen()
	input("""

		All your ships have been smashed! 

		You are drowning in the ocean. You are drowning....

		The game is over!""")


def print_leader_board(leaders):
	clear_screen()

	print("\n\n\n")
	for leader in leaders:
		print(leader.name+"  :  "+str(leader.games_won))
	input("\n\n\n\n\n")

## BONUS

def stall():
	return input("")

def show_result(result):
	input(result)

def print_statement(statement):
	print(statement)

def fetch_info(prompt):
	return input(prompt)