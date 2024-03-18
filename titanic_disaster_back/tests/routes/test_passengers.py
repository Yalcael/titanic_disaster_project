from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from titanic_disaster.controllers.passenger import PassengerController
from titanic_disaster.dependencies import get_passenger_controller
from titanic_disaster.models.passenger import Passenger, Embarked


def test_get_passengers(
    passenger_controller: PassengerController, app: FastAPI, client: TestClient
):
    def _mock_get_passengers():
        passenger_controller.get_passengers = Mock(
            return_value=[
                Passenger(
                    id=1,
                    survived=True,
                    pclass=1,
                    name="Vincent Lemaire",
                    sex="male",
                    age=24,
                    sibsp=2,
                    parch=1,
                    ticket="AC 3221",
                    fare=50.39,
                    cabin="C21",
                    embarked="S",
                ),
                Passenger(
                    id=2,
                    survived=True,
                    pclass=2,
                    name="Sivir Shurima",
                    sex="female",
                    age=26,
                    sibsp=0,
                    parch=2,
                    ticket="PC 53221",
                    fare=79.39,
                    cabin="G19",
                    embarked="C",
                ),
                Passenger(
                    id=3,
                    survived=False,
                    pclass=3,
                    name="Heimer Dinger",
                    sex="male",
                    age=56,
                    sibsp=3,
                    parch=3,
                    ticket="PC 9224",
                    fare=130.79,
                    cabin="E149",
                    embarked="Q",
                ),
            ]
        )
        return passenger_controller

    app.dependency_overrides[get_passenger_controller] = _mock_get_passengers
    get_passenger_response = client.get("/passenger/")
    assert get_passenger_response.status_code == 200
    assert get_passenger_response.json() == [
        {
            "id": 1,
            "survived": True,
            "pclass": 1,
            "name": "Vincent Lemaire",
            "sex": "male",
            "age": 24,
            "sibsp": 2,
            "parch": 1,
            "ticket": "AC 3221",
            "fare": 50.39,
            "cabin": "C21",
            "embarked": "S",
        },
        {
            "id": 2,
            "survived": True,
            "pclass": 2,
            "name": "Sivir Shurima",
            "sex": "female",
            "age": 26,
            "sibsp": 0,
            "parch": 2,
            "ticket": "PC 53221",
            "fare": 79.39,
            "cabin": "G19",
            "embarked": "C",
        },
        {
            "id": 3,
            "survived": False,
            "pclass": 3,
            "name": "Heimer Dinger",
            "sex": "male",
            "age": 56,
            "sibsp": 3,
            "parch": 3,
            "ticket": "PC 9224",
            "fare": 130.79,
            "cabin": "E149",
            "embarked": "Q",
        },
    ]


def test_get_passenger_by_id(
    passenger_controller: PassengerController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_passenger_by_id():
        passenger_controller.get_passenger_by_id = Mock(
            return_value=Passenger(
                id=1,
                survived=True,
                pclass=1,
                name="Vincent Lemaire",
                sex="male",
                age=24,
                sibsp=2,
                parch=1,
                ticket="AC 3221",
                fare=50.39,
                cabin="C21",
                embarked="S",
            ),
        )
        return passenger_controller

    app.dependency_overrides[get_passenger_controller] = _mock_get_passenger_by_id
    get_passenger_by_id_response = client.get("/passenger/1")
    assert get_passenger_by_id_response.status_code == 200
    assert get_passenger_by_id_response.json() == {
        "id": 1,
        "survived": True,
        "pclass": 1,
        "name": "Vincent Lemaire",
        "sex": "male",
        "age": 24,
        "sibsp": 2,
        "parch": 1,
        "ticket": "AC 3221",
        "fare": 50.39,
        "cabin": "C21",
        "embarked": "S",
    }


def test_create_passenger(
    passenger_controller: PassengerController, app: FastAPI, client: TestClient
) -> None:
    def _mock_create_passenger():
        passenger_controller.create_passenger = Mock(
            return_value=Passenger(
                id=1,
                survived=True,
                pclass=1,
                name="Vincent Lemaire",
                sex="male",
                age=24,
                sibsp=2,
                parch=1,
                ticket="AC 3221",
                fare=50.39,
                cabin="C21",
                embarked="S",
            )
        )
        return passenger_controller

    app.dependency_overrides[get_passenger_controller] = _mock_create_passenger
    create_passenger_response = client.post(
        "/passenger/",
        json={
            "survived": True,
            "pclass": 1,
            "name": "Vincent Lemaire",
            "sex": "male",
            "age": 24,
            "sibsp": 2,
            "parch": 1,
            "ticket": "AC 3221",
            "fare": 50.39,
            "cabin": "C21",
            "embarked": "S",
        },
    )
    assert create_passenger_response.status_code == 200
    assert create_passenger_response.json() == {
        "id": 1,
        "survived": True,
        "pclass": 1,
        "name": "Vincent Lemaire",
        "sex": "male",
        "age": 24,
        "sibsp": 2,
        "parch": 1,
        "ticket": "AC 3221",
        "fare": 50.39,
        "cabin": "C21",
        "embarked": "S",
    }


def test_delete_passenger(
    passenger_controller: PassengerController, app: FastAPI, client: TestClient
) -> None:
    def _mock_delete_passenger():
        passenger_controller.delete_passenger = Mock(
            return_value=Passenger(
                id=1,
                survived=True,
                pclass=1,
                name="Vincent Lemaire",
                sex="male",
                age=24,
                sibsp=2,
                parch=1,
                ticket="AC 3221",
                fare=50.39,
                cabin="C21",
                embarked="S",
            )
        )
        return passenger_controller

    app.dependency_overrides[get_passenger_controller] = _mock_delete_passenger
    delete_passenger_response = client.delete("/passenger/1")
    assert delete_passenger_response.status_code == 204


def test_update_user(
    passenger_controller: PassengerController, app: FastAPI, client: TestClient
) -> None:
    def _mock_update_user():
        passenger_controller.update_passenger = Mock(
            return_value=Passenger(
                id=1,
                survived=True,
                pclass=1,
                name="Vincent Lemaire",
                sex="male",
                age=24,
                sibsp=2,
                parch=1,
                ticket="AC 3221",
                fare=50.39,
                cabin="C21",
                embarked="S",
            )
        )
        return passenger_controller

    app.dependency_overrides[get_passenger_controller] = _mock_update_user
    update_passenger_response = client.patch(
        "/passenger/1",
        json={
            "survived": True,
            "pclass": 1,
            "name": "Vincent Lemaire",
            "sex": "male",
            "age": 24,
            "sibsp": 2,
            "parch": 1,
            "ticket": "AC 3221",
            "fare": 50.39,
            "cabin": "C21",
            "embarked": "S",
        },
    )
    assert update_passenger_response.status_code == 200
    assert update_passenger_response.json() == {
        "id": 1,
        "survived": True,
        "pclass": 1,
        "name": "Vincent Lemaire",
        "sex": "male",
        "age": 24,
        "sibsp": 2,
        "parch": 1,
        "ticket": "AC 3221",
        "fare": 50.39,
        "cabin": "C21",
        "embarked": "S",
    }
