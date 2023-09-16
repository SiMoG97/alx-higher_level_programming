#!/usr/bin/python3
"""
    creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    if states:
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    session.close()
