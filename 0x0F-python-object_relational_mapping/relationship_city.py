#!/usr/bin/python3
""" hey """
from sqlalchemy import Column, Integer, String
from relationship_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """
    h
    e
    y
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
