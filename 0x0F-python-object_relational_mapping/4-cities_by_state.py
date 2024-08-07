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
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        ) as connection:
            db_query = ("SELECT cities.id, cities.name, states.name \
                        FROM cities INNER JOIN states \
                        ON states.id = cities.state_id \
                            ORDER BY cities.id ASC;")
            with connection.cursor() as cursor:
                cursor.execute(db_query)

                rows = cursor.fetchall()
                if rows is not None:
                    for row in rows:
                        print(row)

    except Error as e:
        print(e)
