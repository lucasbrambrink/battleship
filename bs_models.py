## BATTLESHIP MODELS ##
import datetime
import random
from blessings import Terminal
t = Terminal()

## DB
import sqlite3



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

	def take_turn(self): ## This logic is the heart of the AI
		while True:
			
			## this is the I in AI
			for success in self.array_successes:  ##successes are objects
				
				## check existence for neighboring success
				in_line_cell = self.check_in_line(success)
				if in_line_cell != None:
					print("unique in_line_cell sent from ",success.cell)
					self.tries.append(in_line_cell)
					print("in line cell is: ",in_line_cell)
					return in_line_cell
				
				
				## feel out waters
				try_this = success.check_periphery() 
				while try_this != None:
					new_x = success.cell[0] + try_this[0]
					new_y = success.cell[1] + try_this[1]
					new_cell = (new_x,new_y)
					unique = True
					for previous_try in self.tries:
						if previous_try == new_cell:
							unique = False
					if new_x > 9 or new_x < 0 or new_y > 9 or new_y < 0: ##deal with boundary case by adding to list regardless, effectively treating it as a fail
						unique = False
					if unique:
						print("feel_out_surroundings cell: ",new_cell)	
						success.periphery.append(new_cell)
						self.tries.append(new_cell)
						return new_cell
					try_this = success.check_periphery()

			## if both conditions fail, simply revert to unique random
			cell = self._random_cell()
			unique = True
			for previous_try in self.tries:
				if previous_try == cell:
					unique = False
			if unique:
				self.tries.append(cell)
				print("random cell: ",cell)
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

	def check_in_line(self,success):
		if len(success.directions_explored) >= 2:
			return None
		tries = {"1": (-1,0),"2":(0,1),"3":(1,0),"4":(0,-1)}
		for i in range(1,5):
			x_cell = success.cell[0] + tries[str(i)][0]
			y_cell = success.cell[1] + tries[str(i)][1]
			test_cell = (x_cell,y_cell)
			for other_success in self.array_successes:
				if other_success.cell == test_cell: ## if true, this means cells align
					if len(success.directions_explored) == 1:
						print(success.cell," has only one direction explored")
						output_x = success.cell[0] - tries[str(i)][0]
						output_y = success.cell[1] - tries[str(i)][1] ## simply extend build by one cycle
						output_cell = (output_x,output_y)
						
						unique = True
						for previous_try in self.tries:
							if previous_try == output_cell:
								unique = False
						if output_cell[0] > 9 or output_cell[0] < 0 or output_cell[1] > 9 or output_cell[1] < 0: ##deal with boundary case by adding to list regardless, effectively treating it as a fail
							unique = False
						if unique:
							print("check in line returned ",output_cell)
							success.accept_direction("+1") ##tell fringe success that it has been extended
							success.accept_completion() ## tell current success
							return output_cell

					else:
						output_x = x_cell + tries[str(i)][0]
						output_y = y_cell + tries[str(i)][1] ## simply extend build by one cycle
						output_cell = (output_x,output_y)
					
						unique = True
						for previous_try in self.tries:
							if previous_try == output_cell:
								unique = False
						if output_cell[0] > 9 or output_cell[0] < 0 or output_cell[1] > 9 or output_cell[1] < 0: ##deal with boundary case by adding to list regardless, effectively treating it as a fail
							unique = False
						if unique:
							print("check in line returned ",output_cell)
							other_success.directions_explored.append("+1")
							other_success.directions_explored.append("completed") ##this cell is now sufficently explored
							## the cell can no longer be len==1
							
							##tell fringe success that it has been extended
							success.directions_explored.append("+1")
							success.accept_completion() ## tell current success
							return output_cell
		return None




class Success: ## for the AI, we turn a successful cell (i.e. hit) into an object
	def __init__(self, cell):
		self.cell = cell ##tuple of location
		self.periphery = [] ## list of tuples
		self.directions_explored = []

	def check_periphery(self):
		if len(self.periphery) < 4:
			# 1 is up, 2 is right, 3 is down, 4 is left
			tries = {"1": (-1,0),"2":(0,1),"3":(1,0),"4":(0,-1)}
			attempt = str(random.randint(1,4)) ## if this produces duplicate, logic will repeat
			return tries[attempt]
		return None

	def accept_direction(self,direction):
		self.directions_explored.append(direction)

	def accept_completion(self):
		for i in range(0,5): ## might only need 3 cycles, but 4 makes double sure
			self.periphery.append('fake')



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
		self.sunken_ships = []

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

		




