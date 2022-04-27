""" Config class employ cool pydantic settings 
    Variables afre fetched  from ENV if present, otherwiese uses values from 
    config classes
    Also you can define differenet config for DEV,TEST etc. 
    Actual config is defined in ENV variable
"""
import os
from typing import Union

from pydantic import BaseSettings


class Base(BaseSettings):
    HOST: str = 'localhost'


class Dev(Base):
    PORT: int = 50050


class Prod(Base):
    PORT = 50050


config = dict(
    dev=Dev,
    prod=Prod
)
settings: Union[Dev, Prod] = config[os.environ.get('ENV', 'dev').lower()]()
