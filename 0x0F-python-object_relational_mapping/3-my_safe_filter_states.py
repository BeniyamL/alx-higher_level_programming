#!/usr/bin/python3
""" a python script to list all states where name matches
    the argument provided from hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """ main function to make the code not to be executed when imported
        it first create a connection to the database and select all
        states where the names matches the argument
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = %(n)s \
                ORDER BY id ASC", {'n': sys.argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
