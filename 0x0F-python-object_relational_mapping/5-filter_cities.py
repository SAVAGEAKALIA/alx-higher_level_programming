#!/usr/bin/python3
"""
This script connects to a MySQL database
and retrieves the names of cities
from the 'cities' table where
the corresponding state name from the 'states' table
matches the provided argument.
Results are sorted in ascending order by 'cities.id'.

Usage:
./script_name.py <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username  : MySQL database username
    mysql_password  : MySQL database password
    database_name   : Name of the MySQL database to connect to
    state_name      : Name of the state to filter cities by
"""

import MySQLdb
import sys


def main():
    """
    Main function that executes the script's logic.
    Connects to the MySQL database,
    executes the query to find cities in a specific state,
    and prints the city names in the format specified.
    """
    # Retrieve command-line arguments
    args = sys.argv[1:]
    username, password, database, arg = args

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC;", (args,))

    # Fetch all rows from the executed query
    rows = cur.fetchall()

    # Print the city names in the specified format
    for i, row in enumerate(rows):
        if i < len(rows) - 1:
            print(row[0], end=", ")
        else:
            print(row[0])

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
