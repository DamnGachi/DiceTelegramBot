
import sqlite3

connect = sqlite3.connect("Dice.db")
cursor = connect.cursor()


cursor.execute("INSERT or REPLACE INTO info (id,player_name) VALUES (1,'mamyebal')")
value = cursor.execute("SELECT * FROM info")
connect.commit()
