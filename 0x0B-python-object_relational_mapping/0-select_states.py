#!/usr/bin/python3
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user="root", passwd="usaUSA777", db="hbtn_0e_0_usa")
    c = db.cursor()
    c.execute("""SELECT id name FROM states ORDER BY id ASC""")
    records = c.fetchall()
    for record in records:
        print(record)
