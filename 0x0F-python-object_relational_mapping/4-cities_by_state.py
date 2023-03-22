#!/usr/bin/python3
""" module lists all cities """

import MySQLdb
import sys

if __name__ == '__main__':

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cur = db.cursor()

    query = "SELECT cities.id, cities.name, \
    states.name FROM cities JOIN states \
    ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
