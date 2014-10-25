## BATTLESHIP CONTROLLER ##
import bs_views
import bs_models
import random
from blessings import Terminal
t = Terminal()

class Controller:
	def __init__(self):
		self.name = None
		self.current_game = None
		self.shooting_board = None
		self.ai_board = None

	def sign_in(self):
		name = bs_views.sign_in()
		self.name = name
		##check if in database.
		self.main_menu()
	
	def main_menu(self):
		proceed = bs_views.main_menu()
		if proceed == "1":
			self.start_new_game()
		if proceed == "2":
			pass
		if proceed == "3":
			pass
		if proceed == "4":
			bs_views.sign_out()
			quit()
		else:
			self.main_menu()

	def start_new_game(self):
		##Initialize Boards
		self.current_game = bs_models.GameBoard()
		self.shooting_board = bs_models.GameBoard()
		self.ai_board = bs_models.GameBoard()
		self.current_game.make_board()
		self.shooting_board.make_board()
		self.ai_board.make_board()

		##Initialize AI
		computer = bs_models.AI()



		

		##Start Game:
		array = ["cruiser1","cruiser2","destroyer1","destroyer2","submarine1","aircraftcarrier1"]
		#self.place_all_boats(array)
		##Run Game:
		self.run_game()




	def run_game(self):
		while True:
			self.turn()
			




	def ai_turn(self):
		bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
		cell = (11,11)
		while cell[0] > 9 or cell[0] < 0 or cell[1] > 9 or cell[1] < 0:
			cell = computer.take_turn()
		if self.current_game.take_turn() == 'duplicate':
			print("OMG")


	def turn(self):
		bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
		x,y = bs_views.take_shot()
		event = self.shooting_board.take_turn(x,y)
		if event == "hit":
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			bs_views.show_result("He's been hit!")
		elif event == "miss":
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			bs_views.show_result("You missed!")
		else:
			bs_views.show_result("You already tried there!")
			self.turn()


	def place_all_boats(self,remaining_boats):
		if len(remaining_boats) == 0:
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			bs_views.placed_all_boats()
		else:
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			boat = bs_models.Boat(bs_views.ask_boat(remaining_boats))
			x,y,orientation = bs_views.place_boat(boat.name)
			test_boat = self.current_game.improper_boat_check(boat.length,x,y,self.current_game.get_orientation_array(orientation))
			if test_boat == "outside_scope":
				bs_views.outside_scope()
			elif test_boat == "not_water":
				bs_views.not_water()
			elif test_boat == "pass":
				bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
				self.current_game.place_boat(boat,x,y,orientation)
				try:
					remaining_boats.remove(boat.name+"1")
				except:
					remaining_boats.remove(boat.name+"2")
			self.place_all_boats(remaining_boats)

		
			


Controller().sign_in()
