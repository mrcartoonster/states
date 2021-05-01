# -*- coding: utf-8 -*-
# Config File
import logging
from functools import lru_cache

from deta import Deta
from environs import Env
from pydantic import BaseSettings
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(messages)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True)],
)

log = logging.getLogger("uvicorn")

env = Env()
env.read_env()

detas = Deta(env("PROJECT_KEY"))


class Settings(BaseSettings):
    """
    Basic envrionment settings.
    """

    deta: str = detas.Deta(env("PROJECT_KEY"))

    class Config:
        """
        Reading .env file.
        """

        env_file = ".env"


@lru_cache()
def get_settings():
    """
    Function for settings.
    """
    log.info("Loading BaseSettings now.")
    return Settings()
