#!/usr/bin/python3
""" module all states """
import MySQLdb
import sys

"""module script to list all the states in a db in ascending order by id
take commandline arguments for mysql username, password and database name"""


if __name__ == '__main__':

    mysql_user, mysql_password, mysql_db = sys.argv[1:]
    # connect to the mysql server
    db = MySQLdb.connect(
            host="localhost",
            user=mysql_user, passwd=mysql_password, db=mysql_db)

    cursor = db.cursor()
    # Execute the SQL query to fetch all states from the database
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # fetch all the rows returned by the query
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # close the cursor and database connections
    cursor.close()
    db.close()
