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

		c.execute("""CREATE TABLE IF NOT EXISTS players
			(id INTEGER, name TEXT, games_won INTEGER, time_created TEXT, PRIMARY KEY ('id'))""")

		c.execute("""CREATE TABLE IF NOT EXISTS games
			(id INTEGER, player_id INTEGER, game_board TEXT, time_created TEXT, PRIMARY KEY ('id'))""")
		
		conn.commit()
		c.close()


## call once to initialize DB
DB().initialize_tables()