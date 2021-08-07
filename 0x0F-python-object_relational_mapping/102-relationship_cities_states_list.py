#!/usr/bin/python3
""" a python script that list all cities object """

import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it lists all cites object
        from the given database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for ct in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(ct.id, ct.name, ct.state.name))
    session.close()
