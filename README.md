Titanic Disaster Visualization

This project aims to visualize data from the Titanic disaster using FastAPI for the backend and NextJS for the frontend.

Tech Stack:

- Backend:
  - Python 3.12
  - FastAPI

- Frontend:
  - NextJS 16.8+

- Database:
  - SQLite (default for FastAPI)

- Containerization:
  - Docker and docker-compose

Getting Started:

1. Clone this repository:

  git clone https://github.com/Yalcael/titanic_disaster_project.git

2. Navigate to the project directory:

cd titanic_disaster_project

3. You should download the train.csv there:
   
https://www.kaggle.com/c/titanic/data?select=train.csv // You should put it in the route of the project.

4. Build and run the project using Docker Compose:

docker-compose up --build

5. Access the frontend at http://localhost:3000 and the backend API at http://localhost:8000.

Functionality:

- Backend:
  - I made a script that fill an SQLite database, I fill it through the train.csv file.
  - I made the backend with a structure of models(Database SQL Models), controllers(The logic) and routes(What will permit the front to call the API).
  - I made some unit-test with Pytest.
  - Used of linter Black and Ruff.
  - I made a Dockerfile.

- Frontend:
  - Displays a table with information about the passengers of the Titanic with TanStack library.
  - Includes a graph with chart.js to represent one of the fields of the dataset.
  - Allows filtering of the displayed data table.
  - I made a Dockerfile.

Dataset:

The Titanic dataset used in this project can be found on Kaggle here: https://www.kaggle.com/c/titanic/data?select=train.csv. I use the train.csv file.
