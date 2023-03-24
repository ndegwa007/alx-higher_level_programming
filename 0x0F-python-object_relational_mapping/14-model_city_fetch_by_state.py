#!/usr/bin/python3
"""module prints all city
objects from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from model_city import City

if __name__ == '__main__':

    username, password, database = argv[1:]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database))

    Session = sessionmaker(bind=engine)

    with Session() as session:
        query = session.query(State, City).filter_by(City.state_id == state.id).all()
        for row in query:
            print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))

