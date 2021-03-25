import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("db.sqlite3")

cur = con.cursor()

# Return all results of query
cur.execute('SQL')

# Be sure to close the connection
con.close()
