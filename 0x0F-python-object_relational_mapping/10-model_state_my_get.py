#!/usr/bin/python3
""" a python script that prints the State object name
     given as argument from the user
 """

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it prints the State object with
        the name passed as argument from the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    st = session.query(State).filter(State.name == sys.argv[4]).first()
    if st is None:
        print('Not found')
    else:
        print(st.id)
    session.close()
