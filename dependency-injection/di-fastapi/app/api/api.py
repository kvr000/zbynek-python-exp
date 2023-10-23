from dependency_injector.wiring import inject, Provide, Provider
from fastapi import Depends, FastAPI, APIRouter

from app.api.deps import Container, DbContainer
from app.db.database import Database

api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "Hello World"}


@api_router.get("/db/")
@inject
def db(database: Database = Depends(Provide[DbContainer.database])):
    database.getConnection()
    return {"message": "database ok"}
