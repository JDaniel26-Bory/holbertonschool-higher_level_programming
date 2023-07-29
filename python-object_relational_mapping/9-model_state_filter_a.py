#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the letter a
"""


from model_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    a_states = session.query(State).filter(State.name.like("%a%")).all()
    for state in a_states:
        print('{}: {}'.format(state.id, state.name))
    session.close()
