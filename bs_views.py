## Views for Battleship ##
from blessings import terminal


def clear_screen():
	print (Terminal().clear)

def sign_in():
	print("Who is singing in right now?")

def print_statement(statement):
	print(statement)

def fetch_info(prompt):
	return input(prompt)