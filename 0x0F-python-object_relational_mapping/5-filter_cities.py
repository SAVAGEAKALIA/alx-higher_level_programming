#!/usr/bin/python3
"""
SQL ORM FOR PYTHON DATABASES
MySqldb
"""

import MySQLdb
import sys

args = sys.argv[1:]

username, password, database, arg = args

db = MySQLdb.connect(host="localhost", port=3306,
                     user=username, passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT cities.name FROM cities, states "
            "WHERE (cities.state_id = states.id) AND states.name = %s ORDER BY cities.id ASC;", (arg,))

rows = cur.fetchall()

i = 0;

for i, row in enumerate(rows):
    if i < len(rows) - 1:
        print(row[0], end=", ")
    else:
        print(row[0])

cur.close()
db.close()

if __name__ == "__main__":
    pass
