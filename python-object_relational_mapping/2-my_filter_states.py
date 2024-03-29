#!/usr/bin/python3
""" Display all the values in the states table where matches the argument
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], password='', db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '%{}%' \
                ORDER BY id".format(str(argv[4])))
    row = cur.fetchall()
    for state in row:
        print(state)
    cur.close()
    db.close()
