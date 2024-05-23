#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco” from the database.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    california.cities = [City(name="San Francisco")]
    session.add(california)
    session.commit()
    session.close()
