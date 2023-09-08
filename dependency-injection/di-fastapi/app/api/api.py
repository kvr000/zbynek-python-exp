from dependency_injector.wiring import inject, Provide, Provider
from fastapi import Depends, FastAPI, APIRouter

from app.api.deps import Container
from app.db.database import Database

api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "Hello World"}


@inject
@api_router.get("/db/")
def db(database: Provider[Database] = Depends(Provide[Container.db_container.database])):
    database.provider().getConnection()
    return {"message": "database ok"}
