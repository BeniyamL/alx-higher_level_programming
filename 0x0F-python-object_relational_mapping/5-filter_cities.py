#!/usr/bin/python3
""" a python script to list all cities that matches that state name
   from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """ main function to make the code not to be executed when imported
        it first create a connection to the database and select all
        cites that matches the given state name from the given database
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON  states.id = cities.state_id \
                WHERE states.name = %(n)s \
                ORDER BY cities.id ASC", {'n': sys.argv[4]})
    rows = cur.fetchall()
    print(', '.join([row[1] for row in rows]))
    cur.close()
    conn.close()
