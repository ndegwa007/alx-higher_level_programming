#!/usr/bin/python3
""" module filter """
import MySQLdb
import sys
"""module list names in the database by filtering names starting with N"""

if __name__ == "__main__":
    """get the mysql username, password,
    and database name as command-line arguments"""
    username, password, database = sys.argv[1:]

    # connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    # create a cursor object to interact with the database
    cur = db.cursor()

    # execute the SQL query to get all states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    # fetch all the results as a list of tuples
    results = cur.fetchall()

    # print the results in the required format
    for row in results:
        print(row)

    # close the cursor and database connections
    cur.close()
    db.close()
