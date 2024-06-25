#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host='localhost', port=3306,
                     user=username, passwd=password, db=database)
cur = db.cursor()
cur.execute("SELECT * FROM states "
            "WHERE name LIKE 'N%' ORDER BY states.id;")

for row in cur.fetchall():
    print(row)

cur.close()
db.close()

if __name__ == "__main__":
    pass
