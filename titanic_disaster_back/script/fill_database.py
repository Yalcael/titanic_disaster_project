from sqlmodel import Session, SQLModel
import pandas as pd

from titanic_disaster.database import engine
from titanic_disaster.models.passenger import Passenger

SQLModel.metadata.create_all(engine)
csv_file_path = "train.csv"
df = pd.read_csv(csv_file_path)
df.columns = df.columns.str.lower()
df['embarked'] = df['embarked'].fillna('S')
df.rename(columns={"passengerid": "id"}, inplace=True)
data_list = df.to_dict(orient="records")

with Session(engine) as session:
    for data in data_list:
        passenger = Passenger(**data)
        session.add(passenger)
    session.commit()
