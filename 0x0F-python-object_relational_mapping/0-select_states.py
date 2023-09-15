#!/usr/bin/python3
"""print all states from hbtn_0e_0_usa database"""
import MySQLdb
import sys


def printAllStates():
    args = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         charset="utf8"
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    printAllStates()
