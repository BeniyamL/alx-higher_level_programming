#!/usr/bin/python3
""" a python script to list all states with a name starting
    with N from hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """ main function to make the code not to be executed when imported
        it first create a connection to the database and select all
        states starting with N from the given database
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states
                WHERE name like 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
