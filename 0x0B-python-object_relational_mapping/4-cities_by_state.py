#!/usr/bin/python3
""" documentation """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """documentation"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN \
        states ON cities.state_id = states.id ORDER BY cities.id")
    records = c.fetchall()
    for record in records:
        print(record)
