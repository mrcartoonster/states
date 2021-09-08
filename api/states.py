# -*- coding: utf-8 -*-
# States API routes
from typing import List, Optional

from fastapi import APIRouter, Query

from crud.db import get, get_all
from models.state_model import StatesOut

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
        description=(
            "Leave empty to get all the US States or enter at least "
            "two letters of the US state to get abbreviaton."
        ),
    ),
):
    """
    Return US state names with their abbreviations.
    """
    if q:
        return get(q)
    return get_all()
