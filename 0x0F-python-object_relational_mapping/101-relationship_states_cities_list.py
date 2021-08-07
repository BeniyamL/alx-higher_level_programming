#!/usr/bin/python3
""" a python script that lists state object with corresponding cities """

import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it lists the state object with
        the correspondig cities from the given database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for st in session.query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("  {}: {}".format(ct.id, ct.name))
    session.close()
