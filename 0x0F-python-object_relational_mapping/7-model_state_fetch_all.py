#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Session = sessionmaker(bind=engine)
session = Session()

data = session.query(State).all()
for obj in data:
    print("{}: {}".format(obj.id, obj.name))
