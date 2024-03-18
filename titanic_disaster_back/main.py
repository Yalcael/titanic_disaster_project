import uvicorn
from titanic_disaster.api import create_app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
