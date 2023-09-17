#!/usr/bin/python3
"""
    lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

# import sys
# from relationship_state import Base, State
# from relationship_city import City
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# if __name__ == "__main__":
#     args = sys.argv
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
#         args[1], args[2], args[3]), pool_pre_ping=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     if states := session.query(State).order_by(State.id):
#         for state in states:
#             print(f"{state.id}: {state.name}")
#             for city in state.cities:
#                 print(f"    {city.id}: {city.name}")

#     session.close()
