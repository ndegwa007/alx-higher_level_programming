#!/usr/bin/python3
"""module contains a state class model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence

Base = declarative_base()


class State(Base):
    """ model class
    Args:
        Base(class): base class from which all
        mapped class should inherit
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
