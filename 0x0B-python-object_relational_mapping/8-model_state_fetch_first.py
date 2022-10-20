#!/usr/bin/python3
"""documentation"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """documentation"""
    Session = sessionmaker(bind=create_engine
                           ('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                            (argv[1], argv[2], argv[3])))

    session = Session()

    for instance in session.query(State).order_by(State.id)[0:1]:
        print('{}: {}'.format(instance.id, instance.name))
