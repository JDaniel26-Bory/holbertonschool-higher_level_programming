#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                ON states.id= cities.state_id WHERE \
                states.name LIKE BINARY %s ORDER BY cities.id", (argv[4], ))
    row = cur.fetchall()
    print(", ".join(city[0] for city in row))
    cur.close()
    db.close()
