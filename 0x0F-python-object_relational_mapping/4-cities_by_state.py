#!/usr/bin/python3
""" A script that lists all cities. """
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
            database=sys.argv[3]
        ) as connection:
            db_query = ("SELECT FROM * cities ORDER BY cities.id ASC;")
            with connection.cursor() as cursor:
                cursor.execute(db_query)

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

    except Error as e:
        print(e)
