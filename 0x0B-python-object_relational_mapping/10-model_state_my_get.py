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

    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance is None:
        print('Not found')
    else:
        print('{}'.format(instance.id))
