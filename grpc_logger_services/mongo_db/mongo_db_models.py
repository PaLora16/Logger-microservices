# Data models
from enum import Enum

from dataclasses import dataclass


class LogAgenda(Enum):
    DEFAULT = 'DEFAULT'
    HEALTH_CHECK = 'HEALTH_CHECK'


class LogLevel(Enum):
    LOG_LEVEL_NOTSET = 'NOTSET'
    LOG_LEVEL_DEBUG = 'DEBUG'
    LOG_LEVEL_INFO = 'INFO'
    LOG_LEVEL_WARNING = 'WARNING'
    LOG_LEVEL_ERROR = 'ERROR'
    LOG_LEVEL_CRITICAL = 'CRITICAL'


@dataclass
class LogDbModel:
    agenda: int
    level: int
    message: str
