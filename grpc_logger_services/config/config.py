import os
from typing import Union

from pydantic import BaseSettings


class Base(BaseSettings):
    MAX_WORKERS: int = 10
    MONGO_HOST: str = 'localhost'
    MONGO_PORT: int = 27017


class Dev(Base):
    PORT: int = 50050


class Prod(Base):
    PORT = 50051


config = dict(
    dev=Dev,
    prod=Prod
)
settings: Union[Dev, Prod] = config[os.environ.get('ENV', 'dev').lower()]()
