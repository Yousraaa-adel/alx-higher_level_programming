#!/usr/bin/python3
"""
    A script  that contains the class definition of
    a City and an instance Base.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State


Base = declarative_base()


class City (Base):
    """ Representation of the City class. """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
