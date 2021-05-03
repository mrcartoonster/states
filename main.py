# -*- coding: utf-8 -*-
# Main API appliction
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import states
from views import home


def create_application() -> FastAPI:
    """
    FastAPI application instance.
    """
    application = FastAPI(
        title="🇺🇸 State Abbreviations",
        description="A simple API that returns U.S. State abbreviations.",
        version="0.0.1",
    )

    application.include_router(states.router)
    application.include_router(home.router)
    application.mount(
        "/static",
        StaticFiles(directory="static"),
        name="static",
    )

    return application


app = create_application()
