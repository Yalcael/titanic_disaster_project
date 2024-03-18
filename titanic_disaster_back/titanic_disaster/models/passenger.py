from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class Sex(str, Enum):
    male = "male"
    female = "female"


class Embarked(str, Enum):
    S = "S"
    Q = "Q"
    C = "C"


class PassengerBase(SQLModel):
    survived: bool
    pclass: int
    name: str
    sex: Sex
    age: int | None = None
    sibsp: int
    parch: int
    ticket: str
    fare: float
    cabin: str | None = None
    embarked: Embarked | None = None


class Passenger(PassengerBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PassengerCreate(PassengerBase):
    pass


class PassengerUpdate(SQLModel):
    survived: bool | None = None
    pclass: int | None = None
    name: str | None = None
    sex: Sex | None = None
    age: int | None = None
    sibsp: int | None = None
    parch: int | None = None
    ticket: str | None = None
    fare: float | None = None
    cabin: str | None = None
    embarked: Embarked | None = None
