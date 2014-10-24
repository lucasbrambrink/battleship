##bs_controller
import bs_views
import bs_models

class Controller:
	def __init__(self):
		self.name = None
		self.current_game = None

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
		self.current_game = bs_models.GameBoard()
		self.current_game.make_board()
		bs_views.print_board(self.current_game.board)
		input("")



Controller().sign_in()
