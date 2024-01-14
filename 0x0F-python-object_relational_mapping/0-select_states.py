#!/usr/bin/python3
""" hey"""
from sys import argv
import MySQLdb
h = "localhost"


def main():
    db = MySQLdb.connect(host=h, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    fetcha = cur.fetchall()
    for fetch in fetcha:
        print(fetch)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
