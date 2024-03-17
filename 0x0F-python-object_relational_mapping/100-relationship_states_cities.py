#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco” 
from the database hbtn_0e_100_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    
    data = session.query(State).filter(State.name == 'California').all()
    
    new_city = City(name='California', state_id=data[0].id)
    session.add(new_city)
    session.commit()
