#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).join(City).all()
    data = session.query(State, City).join(City).all()
    print(type(data[0]))
     for state in data:
         print("{}: {}".format(state.id, state.name))
