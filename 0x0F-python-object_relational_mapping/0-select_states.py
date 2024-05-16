#!/usr/bin/python3

import MySQLdb
from MySQLdb import connect, Error
import sys


if __name__ == "__main__":

    try:
        with connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        ) as connection:
            # print(connection)
            db_query = "SELECT * FROM `states` ORDER BY `states.id` ASC;"
            with connection.cursor() as cursor:
                cursor.execute(db_query)

                rows = cursor.fetchall()
                for row in rows:
                    print(row)

    except Error as e:
        print(e)
