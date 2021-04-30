# -*- coding: utf-8 -*-
from typing import List, Optional

from deta import Deta
from environs import Env
from fastapi import APIRouter, Query
from models.state_model import StatesOut

env = Env()
env.read_env()

deta = Deta(env("PROJECT_KEY"))
db = deta.Base("states")

router = APIRouter(
    prefix="/states",
    tags=["The States"],
)


@router.get("/", response_model=List[StatesOut])
async def states(
    q: Optional[str] = Query(
        None,
        min_length=2,
        max_length=14,
        description="Enter at least the first to letters of the state.",
    ),
):
    """
    Return US state names with their abbreviations.
    """
    if q:
        return next(db.fetch({"states?contains": q.capitalize()}))
    return next(db.fetch())
