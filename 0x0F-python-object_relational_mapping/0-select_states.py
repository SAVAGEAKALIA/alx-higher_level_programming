#!/usr/bin/python3
"""
SQL ORM FOR PYTHON DATABASES

This script connects to a MySQL database
and retrieves all records from the 'states' table
in the specified database.
It orders the results by the 'id' column of the 'states' table.

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
    executes a query to select all records from the 'states' table,
    and prints the retrieved rows.
    """
    # Retrieve command-line arguments
    args = sys.argv[1:]
    username, password, database = args

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all records from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY states.id;")

    # Fetch all rows from the executed query
    rows = cur.fetchall()

    # Print each row retrieved from the 'states' table
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
