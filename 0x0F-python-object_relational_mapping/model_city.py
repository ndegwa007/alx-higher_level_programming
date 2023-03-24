#!/usr/bin/python3
""" module creates model
for table cities"""

from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")
