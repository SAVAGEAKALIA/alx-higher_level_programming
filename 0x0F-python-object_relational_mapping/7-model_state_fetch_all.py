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

    state_name = session.query(State).order_by(State.id.asc()).all()

    for state in state_name:
        print(f"{state.id}: {state.name}")

    # Close session and dispose engine
    session.close()
    engine.dispose()


if __name__ == "__main__":
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    main(engine)
