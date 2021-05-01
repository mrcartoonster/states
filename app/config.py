# -*- coding: utf-8 -*-
# Config File
import logging
from functools import lru_cache

from environs import Env
from pydantic import BaseSettings
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True)],
)

log = logging.getLogger("uvicorn")

env = Env()
env.read_env()


class Settings(BaseSettings):
    """
    Basic envrionment settings.
    """

    deta: str = env("PROJECT_KEY")

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
