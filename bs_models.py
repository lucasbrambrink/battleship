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

	def hit_boat(self):
		self.health -= 1
		if self.health == 0:
			return False
		else:
			return True

class AI:
	def __init__(self):
		self.tries = []
		self.array_successes = []

	def _random_cell(self):
		return (random.randint(0,9),random.randint(0,9))

	def take_turn(self):
		cell = self._random_cell()
		if len(self.tries) != 0:
			for prev_try in self.tries:
				if prev_try == cell:
					self.take_turn()

		if len(self.array_successes) != 0:
			for i in range(0,len(self.array_successes)):
				try_this = self.array_successes[i].check_periphery() 
				if try_this != None:
					self.array_successes[i].periphery.append(try_this)
					return try_this
		return cell

	def accept_success(self,success): ##receives as object
		self.array_successes.append(success)

class Success:
	def __init__(self, cell):
		self.cell = None
		self.periphery = []

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

	def make_board(self):
		self.board = []
		for row in range(0,self.size):
			row = []
			for col in range(0,self.size):
				row.append(t.blue("~ "))
			self.board.append(row)

	def place_boat(self,boat,x,y,orientation): ##must be boat object
		build_specification = {"left":[0,-1,"> ","< ","H "],"right":[0,1,"< ","> ","I "],"up":[-1,0,"V ","A ","H "],"down":[1,0,"A ","V ","H "]}
		length = boat.length
		x_cell,y_cell = (x-1),(y-1)
		while length > 0:
			if length == boat.length:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][2])
			elif length == 1:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][3])
			else:
				self.board[y_cell][x_cell] = t.yellow(build_specification[orientation][-1])
			length -= 1
			y_cell += int(build_specification[orientation][0])
			x_cell += int(build_specification[orientation][1])
		return True

	def get_orientation_array(self,orientation):
		build_specification = {"left":[0,-1,"> ","< ","H "],"right":[0,1,"< ","> ","I "],"up":[-1,0,"V ","A ","H "],"down":[1,0,"A ","V ","H "]}
		return build_specification[orientation]


	## This method returns TRUE if it CANT place the boat
	def improper_boat_check(self,boat_length,x,y,orientation_array):
		test_board_array = self.board
		x -= 1
		y -= 1
		while boat_length > 0:
			if x < 0 or x > 10 or y < 0 or y > 10:
				return 'outside_scope'
			elif test_board_array[y][x] != t.blue("~ "):
				return 'not_water'
			else:
				y += int(orientation_array[0])
				x += int(orientation_array[1])
				boat_length -= 1
		return 'pass'

	def take_turn(self,x,y):
		x_cell,y_cell = x-1,y-1
		if self.board[y_cell][x_cell] != t.blue("~ ") and self.board[y_cell][x_cell] != t.bright_red("X ") and self.board[y_cell][x_cell] != t.cyan("X "):
			self.board[y-1][x-1] = t.bright_red("X ")
			return 'hit'
		elif self.board[y_cell][x_cell] == t.blue("~ "):
			self.board[y-1][x-1] = t.cyan("X ")
			return 'miss'
		else:
			return 'duplicate'

		




