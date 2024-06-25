#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    Main function to execute the script.
    Connects to the MySQL database and queries the 'states' table
    for entries where the name matches a specific pattern.
    """
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE  LOWER(name) LIKE LOWER('N%') ORDER BY states.id;")

    # Fetch all rows from the executed query and print each row
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    # Ensure the main function is called only when the script is executed directly
    main()
