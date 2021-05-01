# -*- coding: utf-8 -*-
# States API routes
from typing import List, Optional

from config import Settings, get_settings
from deta import Deta
from fastapi import APIRouter, Depends, Query
from models.state_model import StatesOut

router = APIRouter(
    prefix="/states",
    tags=["The States"],
)


@router.get("/", response_model=List[StatesOut])
async def states(
    settings: Settings = Depends(get_settings),
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
    deta = settings.deta
    detas = Deta(deta)
    db = detas.Base("states")
    if q:
        return next(db.fetch({"states?contains": q.capitalize()}))
    return next(db.fetch())
