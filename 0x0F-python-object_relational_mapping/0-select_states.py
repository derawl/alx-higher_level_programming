#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3], port=3000)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states')
    row = cursor.fetchall()

    for row in row:
        print(row)