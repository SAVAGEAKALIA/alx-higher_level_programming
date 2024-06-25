#!/usr/bin/python
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys


def main():
    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query using format
    query = "SELECT * FROM states" \
            " WHERE name = '{}' ORDER BY id ASC;".format(state_name)
    cur.execute(query)

    # Fetch and print all rows from the executed query
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
