# -*- coding: utf-8 -*-
# States API routes
from typing import List, Optional

from fastapi import APIRouter, Query

from app.crud.db import get, get_all
from app.models.state_model import StatesOut

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
        return get(q)
    return get_all()
