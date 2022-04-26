# Writes log data to Mongo DB using
from datetime import datetime

from mongo_db.mongo_db_models import LogsDocument
from grpc_logger_pb2 import WriteLogRequest
from mongo_db.mongo_db_services import init_db

# Beanie is fully asynchronous, so we will access it from an async function
async def write_log_to_db(request: WriteLogRequest) -> None:
    await init_db()
    _logrow = LogsDocument(
        agenda=request.log.agenda, level=request.log.level, message=request.log.message, timestamp=datetime.now())
    await _logrow.insert()
