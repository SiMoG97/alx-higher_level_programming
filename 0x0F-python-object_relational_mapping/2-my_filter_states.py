#!/usr/bin/python3
"""
   a script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument. 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         charset="utf8"
                         )
    cur = db.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE name='{args[4]}' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
