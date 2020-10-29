tttBoard = [["X",2,3], [4,"O",6], [7,8,"X"]]
import random
import sqlite3

con = sqlite3.connect('winloss.db')
cur = con.cursor()

cur.execute("""CREATE TABLE win_record (
    name text,
    wins integer,
    loss integer,
    tie integer
    )""")
con.commit()