#!/usr/bin/python3
"""
h
e
y
"""
from sys import argv
import MySQLdb
h = "localhost"


def main():
    db = MySQLdb.connect(host=h, user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
            'N%' ORDER BY id ASC;")
    fall = cur.fetchall()
    for a in fall:
        print(a)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
