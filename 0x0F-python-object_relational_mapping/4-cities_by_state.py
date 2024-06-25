#!/usr/bin/env python
"""
SQL ORM FOR PYTHON DATABASES
MySqldb
"""

import MySQLdb
import sys

args = sys.argv[1:]

username, password, database = args

db = MySQLdb.connect(host="localhost", port=3306,
                     user=username, passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states "
            "WHERE cities.state_id = states.id ORDER BY cities.id ASC;")

for row in cur.fetchall():
    print(row)

cur.close()
db.close()

if __name__ == "__main__":
    pass
