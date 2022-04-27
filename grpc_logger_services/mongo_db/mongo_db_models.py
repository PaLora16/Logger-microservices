# Data models
from datetime import datetime
from beanie import Document, Indexed

#Mongo DB data model required by beanie
class LogsDocument(Document):
    agenda: Indexed(int)
    level: Indexed(int)
    message: str
    timestamp: datetime
