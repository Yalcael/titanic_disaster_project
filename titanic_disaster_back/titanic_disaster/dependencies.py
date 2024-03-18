from fastapi import Depends
from sqlmodel import Session

from titanic_disaster.controllers.passenger import PassengerController
from titanic_disaster.database import engine


def get_session():
    with Session(engine) as session:
        yield session


def get_passenger_controller(session=Depends(get_session)):
    return PassengerController(session)
