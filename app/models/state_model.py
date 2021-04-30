# -*- coding: utf-8 -*-
from pydantic import BaseModel


class StatesIn(BaseModel):
    abbr: str
    key: str
    states: str


class StatesOut(BaseModel):
    abbr: str
    states: str
