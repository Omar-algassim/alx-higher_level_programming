#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import sessionmaker
import sys

user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]
engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(user, passwd, db))
Base = declaritive_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
Base.metadata.create_all(engine)
