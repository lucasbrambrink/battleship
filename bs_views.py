## VIEWS FOR BATTLESHIP GAME ##
from blessings import Terminal

## GLOBAL FUNCTIONS
def clear_screen():
	print (Terminal().clear)

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

def print_board(game_board):
	for row in game_board:
		print("".join(row))


## BONUS:

def print_statement(statement):
	print(statement)

def fetch_info(prompt):
	return input(prompt)