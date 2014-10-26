## BATTLESHIP MODELS ##
import datetime
import random
from blessings import Terminal
t = Terminal()

##metaprogramming
## AI 


class Boat:
	def __init__(self,name):
		length_values = {"cruiser": 2, "destroyer": 3, "submarine": 4, "aircraftcarrier": 5}
		self.name = name
		for key in length_values:
			if name == key:
				self.length = length_values[name]
		self.health = self.length
		self.coordinates = []

	def take_hit(self):
		self.health -= 1
		if self.health == 0:
			return True
		else:
			return False

	def assign_coordinates(self,x,y):
		self.coordinates.append((x,y))

class AI:
	def __init__(self):
		self.tries = []
		self.array_successes = []

	def _random_cell(self):
		return (random.randint(0,9),random.randint(0,9))

	def _random_orientation(self):
		orientations = {"1":"up","2":"down","3":"right","4":"left"}
		return orientations[str(random.randint(1,4))]

	def take_turn(self):
		cell = self._random_cell()
		if len(self.tries) != 0:
			for prev_try in self.tries:
				if prev_try == cell:
					self.take_turn()

		if len(self.array_successes) != 0: ##successes are objects
			for success in self.array_successes:
				try_this = success.check_periphery() 
				if try_this != None:
					success.periphery.append(try_this)
					self.tries.append(try_this)
					return try_this
		self.tries.append(cell)
		return cell

	def accept_success(self,success): ##receives as object
		self.array_successes.append(success)

	def place_boats(self,board,remaining_boats): ##board is object
		## get ready for some recursion
		if len(remaining_boats) == 0:
			return board
		else:
			boat = Boat(remaining_boats[0][:-1]) ## simply take the first one 
			x,y = self._random_cell()
			orientation = self._random_orientation()
			test_boat = board.improper_boat_check(boat.length,x,y,board.get_orientation_array(orientation))
			if test_boat == "pass":
				## actually update the board
				board.place_boat(boat,x,y,orientation)
				try:
					remaining_boats.remove(boat.name+"1")
				except:
					remaining_boats.remove(boat.name+"2")
			self.place_boats(board,remaining_boats)


class Success:
	def __init__(self, cell):
		self.cell = None
		self.in_line = []
		self.periphery = []

	def check_in_line(self):
		pass

	def check_periphery(self):
		if len(self.periphery) < 4:
			# 1 is up, 2 is right, 3 is down, 4 is left
			tries = {"1": (-1,0),"2":(0,1),"3":(1,0),"4":(0,-1)}
			attempt = str(random.randint(len(self.periphery),4))
			return tries[attempt]
		return None



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
		self.boat_list = []

	def make_board(self):
		self.board = []
		for row in range(0,self.size):
			row = []
			for col in range(0,self.size):
				row.append(t.blue("~ "))
			self.board.append(row)

	def place_boat(self,boat,x_cell,y_cell,orientation): ##must be boat object
		build_specification = {"left":[0,-1,"> ","< ","H "],"right":[0,1,"< ","> ","I "],"up":[-1,0,"V ","A ","H "],"down":[1,0,"A ","V ","H "]}
		length = boat.length
		while length > 0:
			if length == boat.length:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][2])
			elif length == 1:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][3])
			else:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][-1])
			boat.assign_coordinates(x_cell,y_cell)
			length -= 1
			y_cell += int(build_specification[orientation][0])
			x_cell += int(build_specification[orientation][1])
		self.boat_list.append(boat)
		return True

	def get_orientation_array(self,orientation):
		build_specification = {"left":[0,-1,"> ","< ","H "],"right":[0,1,"< ","> ","I "],"up":[-1,0,"V ","A ","H "],"down":[1,0,"A ","V ","H "]}
		return build_specification[orientation]


	## This method returns TRUE if it CANT place the boat
	def improper_boat_check(self,boat_length,x,y,orientation_array):
		test_board_array = self.board
		while boat_length > 0:
			if x < 0 or x > 9 or y < 0 or y > 9:
				return 'outside_scope'
			elif test_board_array[y][x] != t.blue("~ "):
				return 'not_water'
			else:
				y += int(orientation_array[0])
				x += int(orientation_array[1])
				boat_length -= 1
		return 'pass'

	def take_turn(self,x,y):
		x_cell,y_cell = x,y
		if self.board[y_cell][x_cell] != t.blue("~ ") and self.board[y_cell][x_cell] != t.bright_red("X ") and self.board[y_cell][x_cell] != t.cyan("X "):
			self.board[y_cell][x_cell] = t.bright_red("X ")
			return 'hit'
		elif self.board[y_cell][x_cell] == t.blue("~ "):
			self.board[y_cell][x_cell] = t.cyan("X ")
			return 'miss'
		else:
			return 'duplicate'

		




