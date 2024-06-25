#!/usr/bin/python3
"""
SQL ORM for Python Databases using MySQLdb

This script connects to a MySQL database and retrieves rows from the 'states'
table where the 'name' matches a user-provided argument. The results are
ordered by 'id'.

Usage:
    ./script_name.py <username> <password> <database> <state_name>

Example:
    ./script_name.py root mypassword mydatabase Texas
"""

import MySQLdb
import sys


def main():
    # Get command-line arguments
    args = sys.argv[1:]

    if len(args) != 4:
        print("Usage: ./script_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = args

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id;"
    cur.execute(query, (state_name,))

    # Fetch and print all rows from the executed query
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
