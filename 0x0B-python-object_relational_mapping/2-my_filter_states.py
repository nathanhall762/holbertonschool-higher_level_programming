#!/usr/bin/python3
""" documentation """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """documentation"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    state = argv[4]
    c.execute("SELECT * FROM states WHERE name = (%s) ORDER BY id ASC",
              (state,))
    records = c.fetchall()
    for record in records:
        print(record)
