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

		Who is singing in right now?\n
		""")

def sign_out():
	clear_screen()
	print("""
		Thank you! I hope you had fun!
		""")


## MENU VIEWS

def main_menu():
	clear_screen()
	print("""Main Menu:

		[1] Start a New Game
		[2] Resume Last Game
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
	while x > 10 or x < 0:
		x = input("X Coordinate: ")
		try:
			x = int(x)
		except:
			x = 11
	while y > 10 or y < 0:
		y = input("Y Coordinate: ")
		try:
			y = int(y)
		except:
			y = 11
	while orientation != "left" and orientation != "right" and orientation != "down" and orientation != "up":
		orientation = input("""How would you like to orient the boat?
			choose [left, right, up or down]
			""")
	return x,y,orientation

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
	while x > 10 or x < 0:
		x = input("X Coordinate: ")
		try:
			x = int(x)
		except:
			x = 11
	while y > 10 or y < 0:
		y = input("Y Coordinate: ")
		try:
			y = int(y)
		except:
			y = 11
	return x,y




## BONUS

def stall():
	return input("")

def show_result(result):
	input(result)

def print_statement(statement):
	print(statement)

def fetch_info(prompt):
	return input(prompt)