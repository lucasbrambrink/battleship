## BATTLESHIP CONTROLLER ##
import bs_views
import bs_models
import random
from blessings import Terminal
t = Terminal()

class Battleship:
	def __init__(self):
		self.name = None
		self.current_game = None
		self.shooting_board = None
		self.ai_board = None
		self.computer = None
		self.komputer = None
		self.player_boats = []
		self.player = None

	def sign_in(self):
		name_player = bs_views.sign_in()
		self.name = name_player
		##check if in database.
		check_statement = "name="+name_player
		returning_player = bs_models.Player.get(check_statement)
		print(returning_player)
		if returning_player != "Not in database":
			bs_views.welcome_back(returning_player.name)
		else:
			self.player = bs_models.Player()
			self.player.accept_name(name_player)
			bs_views.initial_visit(name_player)
			self.player.save()
		self.main_menu()
	
	def main_menu(self):
		proceed = bs_views.main_menu()
		if proceed == "1":
			self.start_new_game()
		if proceed == "2":
			self.battle_ai()
		if proceed == "3":
			self.view_leaderboard()
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

		##Initialize AI              (...spooky. don't worry, he's not 777)
		self.computer = bs_models.AI()
		self.computer_board = bs_models.GameBoard()
		self.computer_board.make_board()
		

		##Start Game:
		## [1.] AI Places boats
		array = ["cruiser1","cruiser2","destroyer1","destroyer2","submarine1","aircraftcarrier1"]
		self.computer.place_boats(self.computer_board,array)
		

		## [2.] Player places boats
		self.decide_boat_placement()


		## [3.] Initalize Turn-Based Game
		self.run_game()

	def battle_ai(self):
		self.computer = bs_models.AI()
		self.komputer = bs_models.AI()
		self.computer_board = bs_models.GameBoard()
		self.computer_board.make_board()
		self.komputer_board = bs_models.GameBoard()
		self.komputer_board.make_board()
		
		array = ["cruiser1","cruiser2","destroyer1","destroyer2","submarine1","aircraftcarrier1"]
		self.computer.place_boats(self.computer_board,array)
		array = ["cruiser1","cruiser2","destroyer1","destroyer2","submarine1","aircraftcarrier1"]
		self.komputer.place_boats(self.komputer_board,array)
		
		while True:
			self.com_ai_turn()
			self.kom_ai_turn()


	def decide_boat_placement(self):
		array = ["cruiser1","cruiser2","destroyer1","destroyer2","submarine1","aircraftcarrier1"]
		decision = bs_views.prompt_boat_placement()
		if decision == 1:
			self.place_all_boats(array)
		else:
			self.computer.place_boats(self.current_game,array)


	def run_game(self):
		while True:
			self.turn()
			self.ai_turn()


	def ai_turn(self):
		cell = self.computer.take_turn()
		event = self.current_game.take_turn(cell[0],cell[1])
		if event == "hit":
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			for boat in self.current_game.boat_list:
				for coordinate in boat.coordinates:
					if cell == coordinate:
						if boat.take_hit():
							bs_views.sunk_ship(boat.name)
							self.current_game.sunken_ships.append(boat)
							if len(self.current_game.sunken_ships) == len(self.current_game.boat_list):
								self.end_game('loss') 
						else:
							bs_views.hit_ship(boat.name)
							self.computer.accept_success(bs_models.Success(cell))
		else:
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			bs_views.show_result("He missed!")	

	def kom_ai_turn(self):
		cell = self.komputer.take_turn()
		event = self.computer_board.take_turn(cell[0],cell[1])
		if event == "hit":
			bs_views.print_both_boards(self.computer_board.board,self.komputer_board.board)
			for boat in self.computer_board.boat_list:
				for coordinate in boat.coordinates:
					if cell == coordinate:
						if boat.take_hit():
							self.computer_board.sunken_ships.append(boat)
							if len(self.computer_board.sunken_ships) == len(self.computer_board.boat_list):
								self.end_game('loss') 
						else:
							self.computer.accept_success(bs_models.Success(cell))
		else:
			bs_views.print_both_boards(self.computer_board.board,self.komputer_board.board)
			bs_views.show_result("He missed!")	

	def com_ai_turn(self):
		cell = self.computer.take_turn()
		event = self.komputer_board.take_turn(cell[0],cell[1])
		if event == "hit":
			bs_views.print_both_boards(self.computer_board.board,self.komputer_board.board)
			for boat in self.komputer_board.boat_list:
				for coordinate in boat.coordinates:
					if cell == coordinate:
						if boat.take_hit():
							self.komputer_board.sunken_ships.append(boat)
							if len(self.komputer_board.sunken_ships) == len(self.komputer_board.boat_list):
								self.end_game('loss') 
						else:
							self.computer.accept_success(bs_models.Success(cell))
		else:
			bs_views.print_both_boards(self.computer_board.board,self.komputer_board.board)
			bs_views.show_result("He missed!")

	def turn(self):
		bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
		x,y = bs_views.take_shot()
		if x == "exit":
			self.question_to_save()
		cell = (x,y)
		event = self.computer_board.take_turn(x,y)
		if event == "hit":
			self.shooting_board.board[y][x] = t.bright_red("X ")
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			for boat in self.computer_board.boat_list:
				for coordinate in boat.coordinates:
					if cell == coordinate:
						if boat.take_hit():
							bs_views.sunk_opponent_ship(boat.name)
							self.computer_board.sunken_ships.append(boat)
							if len(self.computer_board.sunken_ships) == len(self.computer_board.boat_list):
								self.end_game('win')
						else:
							bs_views.show_result("He's been hit!")
		elif event == "miss":
			self.shooting_board.take_turn(x,y)
			bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
			bs_views.show_result("You missed!")
		else:
			bs_views.show_result("You already tried there!")
			self.turn()

	def place_all_boats(self,remaining_boats):
	## use of recursion --> passing in updated array until base-case is reached
	## decided to leave logic in controller bc it directly depends on user input and the separation would only make life difficult when errors are encountered

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
				## actually update the board
				bs_views.print_both_boards(self.current_game.board,self.shooting_board.board)
				self.current_game.place_boat(boat,x,y,orientation)
				try:
					remaining_boats.remove(boat.name+"1")
				except:
					remaining_boats.remove(boat.name+"2")
			self.place_all_boats(remaining_boats)

	def end_game(self,result):
		if result == 'win':
			bs_views.end_game_win()
			self.player.games_won += 1
		else:	
			bs_views.end_game_loss()
		self.main_menu()

	def question_to_save(self):
		response = bs_views.question_to_save()
		if response.lower() == 'yes' or response.lower() == 'y':
			self.save_game()
			self.main_menu()
		else:
			quit()




	## ALL DB LOGIC
	def save_game(self): ##needs a lot of conversions of data types
		player_id = self.fetch_id(self.player,"name",self.name)
		if player_id != None:
			self.current_game.player_id = int(player_id)
		
		self.convert_board_arrays(self.current_game)
		self.current_game.save()
		
		if player_id != None:
			self.shooting_board.player_id = int(player_id)
		
		self.convert_board_arrays(self.shooting_board)
		self.shooting_board.save()
		
		self.computer.convert_arrays()
		self.computer.save()

		# ai_id = self.fetch_id(self.computer,"tries",self.computer.tries)
		# if ai_id != None:
		# 	self.ai_board.player_id = ai_id
		self.convert_board_arrays(self.ai_board)
		self.ai_board.save()
		the_game = bs_models.Games(player_id,0)

	def convert_board_arrays(self,board):
		board.board = str(board.board)
		board.boat_list = str(board.boat_list)
		board.sunken_ships = str(board.sunken_ships)

	def fetch_id(self,objct,unique_attribute,value):
		query = '\''+unique_attribute+"="+value+'\''
		if objct != None:
			test = objct.get(query)
			if test != None:
				return test.id
			else:
				return None

	def view_leaderboard(self):
		leaders = bs_models.Player().all()
		print(leaders)
		print(self.player)
		bs_views.print_leader_board(leaders)
		self.main_menu()





			


Battleship().sign_in()
