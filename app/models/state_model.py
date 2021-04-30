# -*- coding: utf-8 -*-
from pydantic import BaseModel


class StatesOut(BaseModel):
    abbr: str
    states: str
