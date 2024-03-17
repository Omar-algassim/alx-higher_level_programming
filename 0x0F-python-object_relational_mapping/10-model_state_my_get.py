#!/usr/bin/python3
"""print the row contain 'A' in the table"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name == f"{sys.argv[4]}").all()
    if len(data) < 1:
        print("Not found")
    for row in data:
        print(row.id)
