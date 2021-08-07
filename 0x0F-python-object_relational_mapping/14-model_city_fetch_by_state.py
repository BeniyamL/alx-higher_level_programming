#!/usr/bin/python3
""" a python script that prints all city object from the hbtn_0e_0_usa """

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and prints all city object from fiven database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    StateCity = session.query(State, City)\
                       .filter(State.id == City.state_id)\
                       .order_by(City.id).all()
    for s, c in StateCity:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
