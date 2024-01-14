#!/usr/bin/python3
""" hey"""
from sys import argv
import MySQLdb
h = "localhost"


def main():
    db = MySQLdb.connect(host=h, user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC;")
    fetcha = cursor.fetchall()
    for fetch in fetcha:
        print(fetch)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
