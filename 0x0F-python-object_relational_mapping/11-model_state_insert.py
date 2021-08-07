#!/usr/bin/python3
""" a python script that adds the State object to  the hbtn_0e_0_usa """

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it adds the State object "Louisiana"
        to the given database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
    session.close()
