#!/usr/bin/python3
""" a python script that prints the first State object
    from the hbtn_0e_0_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it prints the first State oject
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    st = session.query(State).first()
    if st is None:
        print('Nothing')
    else:
        print("{}: {}".format(st.id, st.name))
    session.close()
