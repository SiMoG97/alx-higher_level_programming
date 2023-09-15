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
        """
            SELECT * FROM states
            WHERE BINARY name = '{}'
            ORDER BY id ASC
        """.format(args[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
