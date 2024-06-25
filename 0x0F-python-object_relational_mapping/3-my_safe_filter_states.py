#!/usr/bin/python3
"""
This script connects to a MySQL database
and retrieves all rows from the 'states' table
where the 'name' column matches the given argument.
The results are sorted in ascending
order by the 'id' column.

Arguments:
    mysql_username  : MySQL database username
    mysql_password  : MySQL database password
    database_name   : Name of the MySQL database to connect to
    state_name      : Name of the state to search
"""

import MySQLdb
import sys


def main():
    """
    Main function that executes the script's logic.
    Connects to the MySQL database,
    executes the query to find matching states,
    and prints each row in the result set.
    """
    # Retrieve command-line arguments
    args = sys.argv[1:]
    username, password, database, arg = args

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = %s ORDER BY states.id;", (arg,))

    # Fetch all rows from the executed query and print each row
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
