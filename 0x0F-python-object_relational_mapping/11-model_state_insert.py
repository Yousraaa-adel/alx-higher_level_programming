#!/usr/bin/python3
"""
    A script that adds the State
    object “Louisiana” to the database.
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

    new_state = State(
        name="Louisiana"
    )

    name = "Louisiana"

    session.add(new_state)
    state = session.query(State).filter(
        State.name.like(name)).first()

    print(str(state.id))
    
    session.commit()
    session.close()
