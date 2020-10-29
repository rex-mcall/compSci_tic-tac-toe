import sqlite3

con = sqlite3.connect('winloss.db')
cur = con.cursor()

cur.execute("""CREATE TABLE win_record (
    name text,
    wins integer,
    loss integer,
    tie integer
    )""")
cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", ("computer",0,0,0))
con.commit()
con.commit()
con.close()