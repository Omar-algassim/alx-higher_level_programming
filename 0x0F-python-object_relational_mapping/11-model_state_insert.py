#!/usr/bin/python3
"""create new column in table with name 'Louisiana' and print the id"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')
    session.add(new)
    session.commit()

    data = session.query(State).filter(State.name == 'Louisiana').all()
    for row in data:
        print(row.id)
