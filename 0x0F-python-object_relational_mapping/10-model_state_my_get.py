#!/usr/bin/python3
"""module prints state object
with the name passed as argument
from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
if __name__ == "__main__":
    username, password, database, state_name = argv[1:]

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database))
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).filter_by(name=state_name).first()

        if state is not None:
            print(state.id)
        else:
            print("Not found")
