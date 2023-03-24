#!/usr/bin/python3
"""module prints a new state id
from the database hbtn_0e_6_usa"""

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
        session.add(State(name="Louisiana"))
        session.commit()
        state = session.query(State).filter_by(name="Louisiana").first()
        print(state.id)
