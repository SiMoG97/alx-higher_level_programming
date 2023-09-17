#!/usr/bin/python3
"""
    lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        args[1], args[2], args[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    if states := session.query(State).order_by(State.id):
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    session.close()
