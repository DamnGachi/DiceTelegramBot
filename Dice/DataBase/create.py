import sqlite3

connect = sqlite3.connect("Dice.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS info(
    id PRIMARY KEY,
    player_name VARCHAR(20) NOT NULL,
    balance INT DEFAULT 5000)""")
connect.commit()
