#!/usr/bin/python3
"""
    lists all City objects from the database hbtn_0e_101_usa
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

    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    if cities := session.query(City).order_by(City.id):
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
