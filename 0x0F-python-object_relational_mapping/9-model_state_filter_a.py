#!/usr/bin/python3
"""
    A script that lists all State objects that
    contain the letter a from the database.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        )
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = "%a%"

    states = session.query(State).filter(
        State.name.like(s)).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
