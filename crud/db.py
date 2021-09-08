# -*- coding: utf-8 -*-
# Simple Deta *detabase SDK* setup.
from operator import itemgetter

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
        return next(db.fetch({"states?contains": state.capitalize()}))


def get_all():
    """
    Return all states.
    """
    return sorted(next(db.fetch()), key=itemgetter("abbr"))
