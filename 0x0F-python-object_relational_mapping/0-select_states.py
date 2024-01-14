#!/usr/bin/python3
"""
h
e
y
"""
from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    fall = cur.fetchall()
    for a in fall:
        print(a)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
