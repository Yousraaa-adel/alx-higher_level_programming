#!/usr/bin/python3
""" A script that takes in the name of a state as
    an argument and lists all cities of that state.
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
            state_name = sys.argv[4]
            db_query = ("SELECT cities.name FROM cities \
                        JOIN states ON \
                        states.id = cities.state_id \
                        WHERE states.name = %s")
            with connection.cursor() as cursor:
                cursor.execute(db_query, (state_name, ))
                rows = cursor.fetchall()
                if rows is not None:
                    print(row[0])

    except Error as e:
        print(e)
