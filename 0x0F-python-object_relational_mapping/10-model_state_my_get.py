#!/usr/bin/python3
"""
    A script that prints the State object with
    the name passed as argument from the database.
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
    name = argv[4]

    state = session.query(State).filter(
        State.name.like(name)).order_by(State.id)

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
