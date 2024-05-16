#!/usr/bin/python3
"""
    A script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from MySQLdb import connect, Error
import sys

if __name__ == "__main__":
    try:
        with connect(
            host="localhost",
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
        ) as connection:
            db_query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                        ORDER BY states.id ASC;".format(sys.argv[4]))
            with connection.cursor() as cursor:
                cursor.execute(db_query)

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

    except Error as e:
        print(e)
