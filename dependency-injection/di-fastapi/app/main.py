#!/usr/bin/python3

import logging

from fastapi import FastAPI, Depends
from mangum import Mangum

from app.api.api import api_router
from app.api.deps import Container

if len(logging.getLogger().handlers) > 0:
	# The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
	# `.basicConfig` does not execute. Thus we set the level directly.
	logging.getLogger().setLevel(logging.INFO)
else:
	logging.basicConfig(level=logging.INFO)

container = Container()

app = FastAPI()
app.container = container
app.container.init_resources()

app.include_router(api_router, prefix="")


handler = Mangum(app)
