#!/usr/bin/python3
""" documentation """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """documentation"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name \
              LIKE BINARY 'N%' ORDER BY id ASC")
    records = c.fetchall()
    for record in records:
        print(record)
