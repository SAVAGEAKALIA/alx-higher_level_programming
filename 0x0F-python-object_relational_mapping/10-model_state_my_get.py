#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(engine):
    """
       Main function that lists all State objects from the database.
    """

    # Create Session with sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(State)\
            .filter(State.name == state_check).order_by(State.id.asc()).first()

    if state_name:
        print(f"{state_name.id}")
    else:
        print('Not found')

    # Close session and dispose engine
    session.close()
    engine.dispose()


if __name__ == "__main__":
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    state_check = sys.argv[4]
    Base.metadata.create_all(engine)
    main(engine)
