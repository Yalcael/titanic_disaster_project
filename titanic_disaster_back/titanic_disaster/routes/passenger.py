from http import HTTPStatus

from fastapi import APIRouter, Depends

from titanic_disaster.controllers.passenger import PassengerController
from titanic_disaster.dependencies import get_passenger_controller
from titanic_disaster.models.passenger import (
    Passenger,
    PassengerCreate,
    PassengerUpdate,
)

router = APIRouter(
    prefix="/passenger",
    tags=["passenger"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Passenger])
def get_passengers(
    *, passenger_controller: PassengerController = Depends(get_passenger_controller)
):
    return passenger_controller.get_passengers()


@router.get("/{passenger_id}", response_model=Passenger)
def get_passenger_by_id(
    *,
    passenger_id: int,
    passenger_controller: PassengerController = Depends(get_passenger_controller)
):
    return passenger_controller.get_passenger_by_id(passenger_id)


@router.post("/", response_model=Passenger)
def create_passenger(
    *,
    passenger_create: PassengerCreate,
    passenger_controller: PassengerController = Depends(get_passenger_controller)
):
    return passenger_controller.create_passenger(passenger_create)


@router.delete("/{passenger_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_passenger(
    *,
    passenger_id: int,
    passenger_controller: PassengerController = Depends(get_passenger_controller)
):
    passenger_controller.delete_passenger(passenger_id)


@router.patch("/{passenger_id}", response_model=Passenger)
def update_passenger(
    *,
    passenger_id: int,
    passenger_update: PassengerUpdate,
    passenger_controller: PassengerController = Depends(get_passenger_controller)
):
    return passenger_controller.update_passenger(passenger_id, passenger_update)
