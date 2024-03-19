#!/usr/bin/python3
"""defien class for base model"""
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from relationship_city import City, Base
import sys


class State(Base):
    """state class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")
