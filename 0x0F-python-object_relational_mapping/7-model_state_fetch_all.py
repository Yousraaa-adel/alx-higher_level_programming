#!/usr/bin/python3
"""
    A script that lists all State objects from the database.
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
            )
        )

    Base.metadata.create_all()

    Session = sessionmaker(bind=engine)
    Session = Session()

    for state in session.query(State).order_by(States.id):
        print("{}: {}".format(state.id, state.name))

    session.close()
