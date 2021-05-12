# -*- coding: utf-8 -*-
# Simple Deta *detabase SDK* setup.
from operator import itemgetter

from deta import Deta
from environs import Env

# Create an __init__.py and place the environs and imports there and import the
# db from the __init__.py file to clean this up!
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
            key=itemgetter("abbr"),
        )


def get_all():
    """
    Return all states.
    """
    return sorted(next(db.fetch()), key=itemgetter("abbr"))
