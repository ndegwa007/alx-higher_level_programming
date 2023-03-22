#!/usr/bin/python3
# This module lists all states from the database hbtn_0e_0_usa
import MySQLdb
import sys

"""
a script to list all the states
in a db in ascending order by id
"""

# take commandline arguments for mysql username, password and database name
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
mysql_db = sys.argv[3]

if __name__ == '__main__':
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
