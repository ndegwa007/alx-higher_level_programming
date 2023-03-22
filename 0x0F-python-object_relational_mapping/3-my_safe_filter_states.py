#!/usr/bin/python3

""" module states get statesname """
import MySQLdb
import sys
if __name__ == '__main__':

    username, password, database, statename = sys.argv[1:]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database)
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC'
    cur.execute(query, ('{}%'.format(statename),))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
