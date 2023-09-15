#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
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
    statement = """SELECT c.id, c.name, s.name
                    FROM cities AS c
                    JOIN states AS s
                    ON c.state_id = s.id
                    ORDER BY c.id ASC
                """
    cur.execute(statement)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
