# -*- coding: utf-8 -*-
# Main API appliction
from fastapi import FastAPI
from routers import states


def create_application() -> FastAPI:
    """
    FastAPI application instance.
    """
    application = FastAPI(
        title="🇺🇸 State Abbreviations",
        description="API that returns U.S. State abbreviations.",
        version="0.0.1",
    )

    application.include_router(states.router)

    return application


app = create_application()
