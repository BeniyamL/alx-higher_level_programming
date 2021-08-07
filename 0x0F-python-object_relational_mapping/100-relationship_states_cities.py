#!/usr/bin/python3
""" a python script that creates the state with city from the database """

import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """ main fucntion to make code not to be executed when imported
        it creates a connection and it creates the State "California"
        with the City from the given database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = State(name="California")
    c = City(name="San Francisco")
    s.cities.append(c)

    session.add(s)
    session.commit()
    session.close()
