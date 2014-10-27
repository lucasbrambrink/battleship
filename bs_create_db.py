## BATTLESHIP DATABASE ##

import sqlite3

class DB:
	def __init__(self, db="battleship.db"):
		self.db = db

	#CREATE TABLES
	def initialize_tables(self):
		conn = sqlite3.connect(self.db)
		c = conn.cursor()	

		c.execute("""DROP TABLE IF EXISTS players""")
		c.execute("""DROP TABLE IF EXISTS games""")
		c.execute("""DROP TABLE IF EXISTS game_boards""")
		c.execute("""DROP TABLE IF EXISTS AIs""")
		c.execute("""DROP TABLE IF EXISTS boats""")
		c.execute("""DROP TABLE IF EXISTS successes""")


		c.execute("""CREATE TABLE IF NOT EXISTS players
			(id INTEGER, name TEXT, games_won INTEGER, latest_sign_in TEXT, PRIMARY KEY ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS games
			(id INTEGER, player_id INTEGER, ai_id INTEGER, time_created TEXT, PRIMARY KEY ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS game_board
			(id INTEGER, player_id INTEGER, game_id INTEGER, size INTEGER, board TEXT, boat_list TEXT, sunken_ships TEXT time_created TEXT, PRIMARY KEY ('id'))""")
		
		c.execute("""CREATE TABLE IF NOT EXISTS ai
			(id INTEGER, game_id INTEGER, tries TEXT, array_successes TEXT, PRIMARY KEY ('id'))""")
		
		c.execute("""CREATE TABLE IF NOT EXISTS boats
			(id INTEGER, board_id INTEGER, name TEXT, health INTEGER, coordinates TEXT, PRIMARY KEY ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS successes
			(id INTEGER, ai_id INTEGER, cell TEXT, periphery TEXT, directions_explored TEXT, PRIMARY KEY ('id'))""")
		
	
		conn.commit()
		c.close()


## call once to initialize DB
DB().initialize_tables()