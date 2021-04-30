# -*- coding: utf-8 -*-
from deta import Deta
from environs import Env
from fastapi import FastAPI, Query

env = Env()
env.read_env()

deta = Deta(env("PROJECT_KEY"))
db = deta.Base("states")

app = FastAPI()


@app.get("/")
async def states(q: str = Query(None)):
    """
    Return US state names with their abbreviations.
    """
    if q:
        return next(db.fetch({"states?contains": q.capitalize()}))
    return next(db.fetch())
