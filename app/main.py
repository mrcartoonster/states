# -*- coding: utf-8 -*-
from fastapi import FastAPI
from routers import states

app = FastAPI(
    title="🇺🇸 State Abbreviations",
    description="API that returns U.S. State abbreviations.",
    version="0.0.1",
)


app.include_router(states.router)
