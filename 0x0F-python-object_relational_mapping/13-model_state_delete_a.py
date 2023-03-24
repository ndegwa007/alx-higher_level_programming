#!/usr/bin/python3
""" module deletes State objects
from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1:]

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database))

    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).filter(State.name.like("%a%"))
        deleted = state.delete()
        session.commit()
