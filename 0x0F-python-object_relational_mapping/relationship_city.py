#!/usr/bin/python3
"""
contains the class City.
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


Base = declarative_base()


class City (Base):
    """ Representation of the City class. """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
