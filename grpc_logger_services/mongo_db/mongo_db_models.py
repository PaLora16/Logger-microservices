# Data models
from dataclasses import dataclass
from datetime import datetime

#mnodel class retaining request data from clien
@dataclass
class LogDbModel:
    agenda: int
    level: int
    message: str
    timestamp: datetime
