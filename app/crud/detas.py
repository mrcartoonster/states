# -*- coding: utf-8 -*-
from config import Settings
from deta import Deta

settings = Settings()
detas = Settings.deta
deta = Deta(detas)
db = deta.Base("states")


def get(state):
    """
    Helper function specific state.
    """
    if state:
        return next(db.fetch({"states?contains": state.capitalize()}))


def get_all():
    """
    Return all states.
    """
    return next(db.fetch())
