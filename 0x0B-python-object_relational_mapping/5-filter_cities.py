#!/usr/bin/python3
""" documentation """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """documentation"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN \
        states ON cities.state_id = states.id WHERE states.name \
            LIKE BINARY %(name)s GROUP BY cities.name", {'name': argv[4]})
    records = c.fetchall()
    # for record in records:
    #     print(record)
    # print(c.fetchall())
    if records is not None:
        print(", ".join([record[0] for record in records]))
        # print(record)
