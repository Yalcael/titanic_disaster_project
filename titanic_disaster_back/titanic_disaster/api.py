from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from titanic_disaster.routes.passenger import router as passenger_router


def create_app():
    app = FastAPI()
    app.include_router(passenger_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(NoResultFound)
    async def unicorn_exception_handler(request: Request, exc: NoResultFound):
        return JSONResponse(
            status_code=404,
            content={"message": "Couldn't find requested resource"},
        )

    return app
