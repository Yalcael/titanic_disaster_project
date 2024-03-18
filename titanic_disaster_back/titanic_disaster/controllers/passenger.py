from sqlmodel import select

from titanic_disaster.models.passenger import (
    Passenger,
    PassengerCreate,
    PassengerUpdate,
)


class PassengerController:
    def __init__(self, session):
        self.session = session

    def get_passengers(self) -> list[Passenger]:
        return self.session.exec(select(Passenger)).all()

    def get_passenger_by_id(self, passenger_id: int) -> Passenger:
        return self.session.exec(
            select(Passenger).where(Passenger.id == passenger_id)
        ).one()

    def create_passenger(self, passenger_create: PassengerCreate) -> Passenger:
        new_passenger = Passenger(**passenger_create.dict())
        self.session.add(new_passenger)
        self.session.commit()
        self.session.refresh(new_passenger)
        return new_passenger

    def delete_passenger(self, passenger_id: int) -> None:
        passenger = self.session.exec(
            select(Passenger).where(Passenger.id == passenger_id)
        ).one()
        self.session.delete(passenger)
        self.session.commit()

    def update_passenger(
        self, passenger_id: int, passenger_update: PassengerUpdate
    ) -> Passenger:
        passenger = self.session.exec(
            select(Passenger).where(Passenger.id == passenger_id)
        ).one()
        for key, val in passenger_update.dict(exclude_unset=True).items():
            setattr(passenger, key, val)
        self.session.add(passenger)
        self.session.commit()
        self.session.refresh(passenger)
        return passenger
