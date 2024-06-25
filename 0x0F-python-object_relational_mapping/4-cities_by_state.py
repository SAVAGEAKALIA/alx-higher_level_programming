#!/usr/bin/python3
"""
This script connects to a MySQL database
and retrieves all rows from the 'cities' table,
joining with the 'states' table to include state names.
The results are sorted in ascending
order by the 'cities.id' column.

Usage:
./script_name.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username  : MySQL database username
    mysql_password  : MySQL database password
    database_name   : Name of the MySQL database to connect to
"""

import MySQLdb
import sys


def main():
    """
    Main function that executes the script's logic.
    Connects to the MySQL database,
    executes the query to find cities along with their
    corresponding state names, and prints each row in the result set.
    """
    # Retrieve command-line arguments
    args = sys.argv[1:]
    username, password, database = args

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select city IDs, city names, and state names
    cur.execute("SELECT cities.name, states.name FROM cities, states "
                "WHERE cities.state_id = states.id ORDER BY cities.id ASC;")

    # Fetch all rows from the executed query and print each row
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
