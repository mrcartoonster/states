# -*- coding: utf-8 -*-
from pydantic import BaseModel


class StatesOut(BaseModel):
    """
    Pydantic model to filter out Detabase keys.
    """

    abbr: str
    states: str
