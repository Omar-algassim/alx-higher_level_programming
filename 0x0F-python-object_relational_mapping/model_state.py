#!/usr/bin/python3
"""defien class for base model"""
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
import sys

user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]
engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(user, passwd, db))
Base = declarative_base()


class State(Base):
    """state class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
