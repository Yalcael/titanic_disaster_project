import string

from faker import Faker
from sqlmodel import Session, select
import random
from titanic_disaster.controllers.passenger import PassengerController
from titanic_disaster.models.passenger import (
    Passenger,
    PassengerCreate,
    PassengerUpdate,
    Sex,
    Embarked,
)


def test_create_passenger(
    passenger_controller: PassengerController, session: Session, faker: Faker
) -> None:
    created_passenger = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )
    passengers = session.exec(select(Passenger)).all()
    assert len(passengers) == 1
    assert created_passenger.survived == passengers[0].survived
    assert created_passenger.pclass == passengers[0].pclass
    assert created_passenger.name == passengers[0].name
    assert created_passenger.sex == passengers[0].sex
    assert created_passenger.age == passengers[0].age
    assert created_passenger.sibsp == passengers[0].sibsp
    assert created_passenger.parch == passengers[0].parch
    assert created_passenger.ticket == passengers[0].ticket
    assert created_passenger.fare == passengers[0].fare
    assert created_passenger.cabin == passengers[0].cabin
    assert created_passenger.embarked == passengers[0].embarked


def test_get_passenger_by_id(
    passenger_controller: PassengerController, faker: Faker
) -> None:
    created_passenger = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )
    passenger = passenger_controller.get_passenger_by_id(created_passenger.id)
    assert passenger.id == passenger.id
    assert passenger.survived == created_passenger.survived
    assert passenger.pclass == created_passenger.pclass
    assert passenger.name == created_passenger.name
    assert passenger.sex == created_passenger.sex
    assert passenger.age == created_passenger.age
    assert passenger.sibsp == created_passenger.sibsp
    assert passenger.parch == created_passenger.parch
    assert passenger.ticket == created_passenger.ticket
    assert passenger.fare == created_passenger.fare
    assert passenger.cabin == created_passenger.cabin
    assert passenger.embarked == created_passenger.embarked


def test_get_passengers(
    passenger_controller: PassengerController, faker: Faker
) -> None:
    created_passenger_1 = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )

    created_passenger_2 = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )

    created_passenger_3 = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )
    passengers = passenger_controller.get_passengers()
    assert passengers[0].survived == created_passenger_1.survived
    assert passengers[0].pclass == created_passenger_1.pclass
    assert passengers[0].name == created_passenger_1.name
    assert passengers[0].sex == created_passenger_1.sex
    assert passengers[0].age == created_passenger_1.age
    assert passengers[0].sibsp == created_passenger_1.sibsp
    assert passengers[0].parch == created_passenger_1.parch
    assert passengers[0].ticket == created_passenger_1.ticket
    assert passengers[0].fare == created_passenger_1.fare
    assert passengers[0].cabin == created_passenger_1.cabin
    assert passengers[0].embarked == created_passenger_1.embarked
    assert passengers[1].survived == created_passenger_2.survived
    assert passengers[1].pclass == created_passenger_2.pclass
    assert passengers[1].name == created_passenger_2.name
    assert passengers[1].sex == created_passenger_2.sex
    assert passengers[1].age == created_passenger_2.age
    assert passengers[1].sibsp == created_passenger_2.sibsp
    assert passengers[1].parch == created_passenger_2.parch
    assert passengers[1].ticket == created_passenger_2.ticket
    assert passengers[1].fare == created_passenger_2.fare
    assert passengers[1].cabin == created_passenger_2.cabin
    assert passengers[1].embarked == created_passenger_2.embarked
    assert passengers[2].survived == created_passenger_3.survived
    assert passengers[2].pclass == created_passenger_3.pclass
    assert passengers[2].name == created_passenger_3.name
    assert passengers[2].sex == created_passenger_3.sex
    assert passengers[2].age == created_passenger_3.age
    assert passengers[2].sibsp == created_passenger_3.sibsp
    assert passengers[2].parch == created_passenger_3.parch
    assert passengers[2].ticket == created_passenger_3.ticket
    assert passengers[2].fare == created_passenger_3.fare
    assert passengers[2].cabin == created_passenger_3.cabin
    assert passengers[2].embarked == created_passenger_3.embarked


def test_delete_create_passenger(
    passenger_controller: PassengerController, session: Session, faker: Faker
) -> None:
    created_passenger = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )
    passenger_controller.delete_passenger(created_passenger.id)
    passenger = session.exec(select(Passenger)).all()
    assert len(passenger) == 0


def test_update_passenger_valid_id_and_update(
    passenger_controller: PassengerController, session: Session, faker: Faker
) -> None:
    created_passenger = passenger_controller.create_passenger(
        PassengerCreate(
            survived=bool(random.getrandbits(1)),
            pclass=random.randint(1, 3),
            name=faker.name(),
            sex=random.choice(list(Sex)),
            age=random.randint(1, 100),
            sibsp=random.randint(0, 10),
            parch=random.randint(0, 10),
            ticket=f"ticket {random.randint(1, 10000)}",
            fare=round(random.uniform(1.0, 250.0), 2),
            cabin=f"{random.choice(string.ascii_letters)}{random.randint(0, 100)}",
            embarked=random.choice(list(Embarked)),
        )
    )
    passenger_id = 1
    updated_passenger = passenger_controller.update_passenger(
        created_passenger.id,
        PassengerUpdate(
            name=faker.name(),
            age=random.randint(1, 100),
            sex=random.choice(list(Sex)),
            survived=bool(random.getrandbits(1)),
        ),
    )
    passenger = session.exec(select(Passenger)).all()
    assert isinstance(updated_passenger, Passenger)
    assert passenger[0].id == passenger_id
    assert passenger[0].name == updated_passenger.name
    assert passenger[0].age == updated_passenger.age
    assert passenger[0].sex == updated_passenger.sex
    assert passenger[0].survived == updated_passenger.survived
