#!/usr/bin/python3
""" module prints city names based on state """
import MySQLdb
import sys

if __name__ == '__main__':
    # Check if all 4 arguments are passed in
    if len(sys.argv) != 5:
        print("Usage: {} username \
                password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3], port=3306)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query
    query = "SELECT cities.id, cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            GROUP BY cities.id, cities.name \
            ORDER BY cities.id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the city names
    city_names = [row[1] for row in rows]
    print(', '.join(city_names))

    # Close the cursor and database connection
    cur.close()
    db.close()
