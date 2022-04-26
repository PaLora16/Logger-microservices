# Data models
from datetime import datetime
from beanie import Document, Indexed


class LogsDocument(Document):
    agenda: Indexed(int)
    level: Indexed(int)
    message: str
    timestamp: datetime
