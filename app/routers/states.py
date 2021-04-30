# -*- coding: utf-8 -*-
from typing import List, Optional

import models
from deta import Deta
from environs import Env
from fastapi import APIRouter

env = Env()
env.read_env()

deta = Deta(env("PROJECT_KEY"))
db = deta.Base("states")

router = APIRouter(
    prefix="/states",
    tags=["the states"],
)


@router.get("/", response_model=List[models.StatesOut])
async def states(q: Optional[str] = None):
    """
    Return US state names with their abbreviations.
    """
    if q:
        return next(db.fetch({"states?contains": q.capitalize()}))
    return next(db.fetch())
