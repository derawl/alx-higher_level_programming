#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys



if __name__ == '__main__':
    """
    Connects to database and retrieves all records for states
    """
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3], port=3000)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states')
    row = cursor.fetchall()

    for row in row:
        print(row)