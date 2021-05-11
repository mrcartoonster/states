# -*- coding: utf-8 -*-
# Simple Deta *detabase SDK* setup.
from deta import Deta
from environs import Env

env = Env()
env.read_env()
deta = Deta(env("PROJECT_KEY"))
db = deta.Base("states")


def get(state):
    """
    Helper function specific state.
    """
    if state:
        return sorted(
            next(db.fetch({"states?contains": state.capitalize()})),
            key=lambda x: x["abbr"],
        )


def get_all():
    """
    Return all states.
    """
    return sorted(next(db.fetch()), key=lambda x: x["abbr"])
