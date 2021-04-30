# -*- coding: utf-8 -*-
from fastapi import FastAPI

from .routers import states

app = FastAPI()


app.include_router(states.router)
