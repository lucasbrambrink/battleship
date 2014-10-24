## BATTLESHIP MODELS ##
import datetime



class Boat:
	def __init__(self,name):
		length_values = {"Cruiser": 2, "Destroyer": 3, "Submarine": 4, "Aircraftcarrier": 5}
		self.name = name
		self.length = length_values[name]
		self.health = self.length

	def hit_boat(self):
		self.health -= 1
		if self.health == 0:
			return False
		else:
			return True


class Player:
	def __init__(self,name):
		self.name = name
		self.latest_sign_in = datetime.datetime.now()

	def fetch_ongoing_games(self):
		##check database for games with Uid
		pass


class GameBoard:
	def __init__(self,size=10):
		self.size = size
		self.board = None

	def make_board(self):
		self.board = []
		for row in range(0,self.size):
			row = []
			for col in range(0,self.size):
				row.append("~ ")
			self.board.append(row)

	def shoot_cell(self,x,y):##take arguments starting from 1 for users
		self.board[y-1][x-1] = "X "


	def place_boat(self,boat,x,y,orientation): ##must be boat object
		build_specification = {"left":[0,-1,"> ","< ","H "],"right":[0,1,"< ","> ","I "],"up":[-1,0,"V ","A ","H "],"down":[1,0,"A ","V ","H "]}
		length = boat.length
		x_cell,y_cell = (x-1),(y-1)
		if self.run_placement_check(length,x_cell,y_cell,build_specification[orientation]):
			while length > 0:
				if length == boat.length:
					self.board[y_cell][x_cell] = build_specification[orientation][2]
				elif length == 1:
					self.board[y_cell][x_cell] = build_specification[orientation][3]
				else:
					self.board[y_cell][x_cell] = build_specification[orientation][-1]
					# if orientation == "up" or orientation == "down":
					# 	self.board[y_cell][x_cell-1] = "~"
				length -= 1
				y_cell += int(build_specification[orientation][0])
				x_cell += int(build_specification[orientation][1])
			return True
		else:
			return False

	def run_placement_check(self,boat_length,x,y,orientation_array):
		test_board_array = self.board
		while boat_length > 0:
			if x < 0 or x > 10 or y < 0 or y > 10 or test_board_array[y][x] != "~ ":
				return False
			else:
				y += orientation_array[0]
				x += orientation_array[1]
				boat_length -= 1
		return True

	def place_boats(self):
		pass



