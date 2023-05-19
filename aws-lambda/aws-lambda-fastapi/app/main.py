#!/usr/bin/python3

import logging

from fastapi import FastAPI
from app.api.api import router as api_router
from mangum import Mangum


if len(logging.getLogger().handlers) > 0:
	# The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
	# `.basicConfig` does not execute. Thus we set the level directly.
	logging.getLogger().setLevel(logging.INFO)
else:
	logging.basicConfig(level=logging.INFO)


app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World"}

app.include_router(api_router, prefix="/api")

handler = Mangum(app)
