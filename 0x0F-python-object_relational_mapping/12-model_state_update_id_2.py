#!/usr/bin/python3
""" module updates State object
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
        state = session.query(State).filter_by(id=2).first()
        state.name = "New Mexico"
        session.commit()
