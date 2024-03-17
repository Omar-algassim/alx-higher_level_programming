#!/usr/bin/python3
"""defien class for base model"""
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_city import City
import sys

Base = declarative_base()


class State(Base):
    """state class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state = relationship(City, backref="states")