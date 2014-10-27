## BATTLESHIP DATABASE ##

import sqlite3

class DB:
	def __init__(self, db="battleship.db"):
		self.db = db

	#CREATE TABLES
	def initialize_tables(self):
		conn = sqlite3.connect(self.db)
		c = conn.cursor()	

		c.execute("""DROP TABLE IF EXISTS Player""")
		c.execute("""DROP TABLE IF EXISTS Games""")
		c.execute("""DROP TABLE IF EXISTS GameBoard""")
		c.execute("""DROP TABLE IF EXISTS AI""")
		c.execute("""DROP TABLE IF EXISTS Boat""")
		c.execute("""DROP TABLE IF EXISTS Success""")


		c.execute("""CREATE TABLE IF NOT EXISTS Player
			(id PRIMARY KEY,
			 name TEXT,
			 games_won INTEGER,
			 latest_sign_in TEXT)""")

		c.execute("""CREATE TABLE IF NOT EXISTS Games
			(id PRIMARY KEY, 
			 player_id INTEGER,
			 ai_id INTEGER, 
			 time_created TEXT, 
			 FOREIGN KEY ('ai_id') REFERENCES AI ('id'),
			 FOREIGN KEY ('player_id') REFERENCES Player ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS GameBoard
			(id PRIMARY KEY, 
			 player_id INTEGER, 
			 game_id INTEGER, 
			 size INTEGER, 
			 board TEXT, 
			 boat_list TEXT, 
			 sunken_ships TEXT, 
			 time_created TEXT, 
			 FOREIGN KEY ('player_id') REFERENCES Player ('id')
			 FOREIGN KEY ('game_id') REFERENCES Games ('id'))""")
		
		c.execute("""CREATE TABLE IF NOT EXISTS AI
			(id PRIMARY KEY, 
			 game_id INTEGER, 
			 tries TEXT, 
			 array_successes TEXT, 
			 FOREIGN KEY ('game_id') REFERENCES Games ('id'))""")
		
		c.execute("""CREATE TABLE IF NOT EXISTS Boat
			(id PRIMARY KEY, 
			 board_id INTEGER, 
			 name TEXT, 
			 health INTEGER, 
			 coordinates TEXT, 
			 FOREIGN KEY ('board_id') REFERENCES GameBoard ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS Success
			(id PRIMARY KEY, 
			 ai_id INTEGER, 
			 cell TEXT, 
			 periphery TEXT, 
			 directions_explored TEXT, 
			 FOREIGN KEY ('ai_id') REFERENCES AI ('id'))""")
		
		conn.commit()
		c.close()


## call once to initialize DB
DB().initialize_tables()