#!/usr/bin/python3
"""
    write a script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
from MySQLdb import connect, Error
import sys


if __name__ == "__main__":
    try:
        with connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        ) as connection:
            name_searched = sys.argv[4]
            db_query = ("SELECT * FROM states \
                        WHERE name LIKE BINARY %s \
                        ORDER BY states.id ASC", (name_searched, ))
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                rows = cursor.fetchall()
                if rows is not None:
                    for row in rows:
                        print(row)

    except Error as e:
        print(e)
