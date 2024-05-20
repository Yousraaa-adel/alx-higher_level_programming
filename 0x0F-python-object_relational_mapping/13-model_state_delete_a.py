#!/usr/bin/python3
"""
    A script that deletes all State objects with
    a name containing the letter a from the database.
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
    name = "%a%"

    states = session.query(State).filter(
        State.name.like(name)).one()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
