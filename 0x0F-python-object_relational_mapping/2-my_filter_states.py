#!/usr/bin/python3

import MySQLdb
import sys

args = sys.argv[1:]

username, password, database, arg = args

db = MySQLdb.connect(host="localhost", port=3306,
                     user=username, passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT * FROM states "
            "WHERE name = %s ORDER BY states.id;", (arg,))

for row in cur.fetchall():
    print(row)

cur.close()
db.close()

if __name__ == "__main__":
    pass
